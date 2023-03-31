import logging
import time
import streamlit as st
from decouple import config
from typing import Dict
from helpers.live_or_mock_service import LiveOrMockService

class WebApp:
    def __init__(self):
        self.logger = logging.getLogger("logger")
        self.url_params: Dict[str, str] = st.experimental_get_query_params()
        self.services = LiveOrMockService()
        self.webhook_db = self.services.mongo_client.get_database("webhook_db")
        webhooks = self.webhook_db.get_collection("webhooks")
        if len(self.url_params) == 2:
            self.server_name = self.url_params["discord_server_name"][0] or ""
            self.server_id = self.url_params["id"][0] or ""
            self.webhook_set = len(list(webhooks.find({"server": self.server_id}))) > 0

    def upload_webhook(self):
        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)
        webhook = st.session_state.webhook

        if "https://discord.com/api/webhooks/" not in webhook or len(webhook) != 121:
            latest_iteration.text("Please enter a valid Discord webhook.")
            bar.error("Errored when validating webhook.")

            return

        requests = self.services.requests

        data = {"content": 'Attempting to add webhook...'}
        response = requests.post(webhook, json=data)
        self.logger.info(f"Attempted to configure webhook {webhook} with statuscode: {response.status_code}")

        latest_iteration.text("Attempting to send sample message to Discord channel...")
        bar.progress(33)

        time.sleep(1)

        if response.status_code < 200 or response.status_code > 208:
            latest_iteration.error(f"Could not register the webhook {webhook}, is the URL definitely correct?")
            bar.error("Errored when sending message to discord.")

            return

        latest_iteration.text("Uploading webhook to database...")
        bar.progress(66)

        time.sleep(1)

        registered_webhooks = self.webhooks.find()

        if webhook in [result["registered_webhook"] for result in registered_webhooks]:
            latest_iteration.error(f"The webhook {webhook} has already been registered, returning.")
            bar.error("Errored when uploading to database.")

            return

        if self.server_id in [result["server"] for result in registered_webhooks]:
            latest_iteration.error(f"The webhook {webhook} has already been registered, returning.")
            bar.error("Errored when uploading to database.")

            return

        try:
            self.webhooks.insert_one({"registered_webhook": webhook, "server": self.server_id, "birthdays": []})
            requests.post(webhook, json={"content": f"""Webhook Added! Use this URL to enter birthdays: {config('HOSTNAME')}
                                        ?id={self.server_id}&webhook_set=true&discord_server_name={self.server_name}"""})
            latest_iteration.success("Successfully added webhook for your server!")
            bar.progress(100)

        except Exception as e:
            self.logger.warning(e.message)
            latest_iteration.error("Something went wrong when inserting the webhook into the database, please try again...")
            bar.error("Errored when uploading to database.")

        finally:
            time.sleep(3)
            latest_iteration.empty()
            bar.empty()

    def upload_birthday(self):
        existing_server_birthdays = self.webhooks.find_one({"server": self.server_id})["birthdays"]
        existing_server_birthdays.append({"name": st.session_state.name, "birthday": str(st.session_state.birthday)})
        self.webhooks.update_one({"server": self.server_id}, {"$set": {"birthdays": existing_server_birthdays}})

    def main(self):
        if "discord_server_name" not in self.url_params.keys() or "id" not in self.url_params.keys():
            st.write("# Invalid Url")
            st.image("https://steamuserimages-a.akamaihd.net/ugc/959732343597073737/5FBAF677D6CFDB27481A5F5E2C146F4858F963BA/?imw=5000&imh=5000&ima=fit&"
                     "impolicy=Letterbox&imcolor=%23000000&letterbox=false", use_column_width="always")

            st.write("### Please make sure to use a URL provided by the Discord Bot.")

            return
        
        st.title = "Add a birthday to your server!"
        st.write(f"""# Welcome {self.server_name}!""")

        if not self.webhook_set:
            st.write("""Before you can put in user Birthdays, you have to register a webhook for your server!""")
            st.write("#### You can do this by your server admin nominating a channel in your server, \
                    clicking on the cog icon, going to Integrations and creating a webhook, then they \
                    can finally enter the URL in the following field:")
            st.text_input("Paste your webhook here", key="webhook")
            st.button("Submit Webhook", on_click=self.upload_webhook)
        else:
            st.write("#### All you have to do is enter your name and your birthday!")
            st.text_input("Enter your name:", key="name")
            st.date_input("Enter your birthday:", key="birthday")
            st.button("Enter Birthday", on_click=self.upload_birthday)
            st.image("https://media3.giphy.com/media/zGnnFpOB1OjMQ/200.gif", use_column_width="always")


WebApp().main()
