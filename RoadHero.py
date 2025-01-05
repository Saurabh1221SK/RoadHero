import streamlit as st
import cv2
from datetime import datetime
import numpy as np

def main():
    st.title("Photo Capture with Timestamp")

    img_file_buffer = st.camera_input("Take a picture")

    if img_file_buffer is not None:
        bytes_data = img_file_buffer.getvalue()
        img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, timestamp, (10, img.shape[0] - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        st.image(img, channels="BGR")

        vehicle_number = st.text_input("Enter Vehicle Number:")

        if vehicle_number:
            violations = st.multiselect(
                "Choose traffic violations",
                options=[
                    "Red light jumping",
                    "Helmet violation",
                    "Seat belt violation",
                    "Unauthorized parking",
                    "Overloading",
                    "No entry",
                    "Wrong side driving",
                    "Mobile phone use while driving",
                    "Driving under influence"
                ]
            )

            st.markdown("### Enter the current location (Pincode):")
            pincode = st.text_input("Enter Pincode:")

            if violations:
                st.markdown(f"**Selected Violation(s):** {', '.join(violations)}")

            if pincode:
                st.markdown(f"**Current Location Pincode:** {pincode}")
            else:
                st.warning("Please enter the pincode.")

            st.markdown("### Enter Reporter Bank Account Details:")
            reporter_name = st.text_input("Name:")
            bank_name = st.text_input("Bank Name:")
            account_number = st.text_input("Account Number:")
            ifsc_code = st.text_input("IFSC Code:")

            if reporter_name and bank_name and account_number and ifsc_code:
                st.markdown("**Reporter Bank Details Submitted**")

            if st.button("Submit"):
                st.markdown("### Submission Successful!")
                st.markdown(f"**Vehicle Number:** {vehicle_number}")
                st.markdown(f"**Violations Recorded:** {', '.join(violations)}")
                st.markdown(f"**Timestamp:** {timestamp}")
                st.markdown(f"**Location Pincode:** {pincode}")
                st.markdown(f"**Reporter Name:** {reporter_name}")
                st.markdown(f"**Bank Name:** {bank_name}")
                st.markdown(f"**Account Number:** {account_number}")
                st.markdown(f"**IFSC Code:** {ifsc_code}")
                
                st.markdown("---")
                st.markdown("### Important Note:")
                st.markdown("If the vehicle is found guilty of the reported violations, you will be rewarded accordingly. Thank you for your service!")

        else:
            st.info("Please enter the vehicle number to proceed.")

if __name__ == "__main__":
    main()
