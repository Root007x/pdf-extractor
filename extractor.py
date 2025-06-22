import pymupdf
import json

# Open the signed PDF form for data extraction
docs = pymupdf.open("Form ADT-1-29092023_signed.pdf")

# List of field names to ignore or skip during extraction
target_fields = [
    "TextField","Attach","attachment_L","Acceptance","Submit_B","Prescrutiny_B","CheckForm_B","Modify_B","CheckForm_C",
    "Formid_C","Version_F","CINStatus_N","HiddenList_L","HTF","DesigD_C","CurrDate","ResoNum","LSI", "RegMemberShNum", "DateOfAppSect_D"
]

# Mapping of PDF field names to desired output JSON keys
key_mapping = {
    "PreFill_B": "pre_fill",
    "CIN_C": "cin",
    "CompanyName_C": "company_name",
    "CompanyAdd_C": "registered_office",
    "EmailId_C": "company_email",
    "FormLanguage": "form_language",
    "WhtrCmpnyFallClassOfCmpny": "is_company_classified",
    "WhtrJointAudAppoint": "is_joint_auditor_appointed",
    "AuditorNumber": "auditor_count",
    "DropDownList1": "appointment_type",
    "PAN_C": "auditor_pan",
    "NameAuditorFirm_C": "auditor_name",
    "CategoryOfAuditor": "auditor_category",
    "MemberShNum": "auditor_membership_number",
    "permaddress2a_C": "auditor_address_line1",
    "permaddress2b_C": "auditor_address_line2",
    "City_C": "auditor_city",
    "State_P": "auditor_state",
    "Country_C": "auditor_country",
    "Pin_C": "auditor_pin",
    "email": "auditor_email",
    "DateOfAccAuditedFrom_D": "financial_year_start",
    "DateOfAccAuditedTo_D": "financial_year_end",
    "NumOfFinanYearApp": "financial_years_appointed",
    "WhrtInLimit": "within_limits",
    "NumOfFinanYear": "number_of_financial_years",
    "DateAnnualGenMeet_D": "agm_date",
    "DateReceipt_D": "form_receipt_date",
    "WhrAuditorApp": "auditor_appointment_confirmed",
    "DateOfAppSect_D": "appointment_date_raw",
    "DINOfDir_C": "director_din",
    "WhrCasualAuditor": "is_casual_auditor",
    "Sign1": "signatory_info"
}

# Dictionary to store raw extracted data from the PDF
# and another for the organized output
data = {}
organized_data = {}

# Iterate through each page in the PDF
for page in docs:

    widgets = page.widgets()

    # Iterate through each form widget (field) on the page
    for widget in widgets:
        key = widget.field_name
        field_type = widget.field_type_string
        value = widget.field_value
        rect = widget.rect
        button_state = widget.button_states
        field_key = key.split('.')[-1].split('[')[0]
        text_box_content = page.get_textbox(rect)

        # If the widget is a radio button and selected, store its value
        if widget.field_type == pymupdf.PDF_WIDGET_TYPE_RADIOBUTTON: 
            if value != 'Off':
                data[field_key] = value

        # Skip empty text boxes or fields in the target_fields list
        if not text_box_content or any(word in field_key for word in target_fields):
            continue
        # Clean and store the text box content
        clean_content = ", ".join(line.strip() for line in text_box_content.splitlines())
        data[field_key] = clean_content

# Map the extracted data to the organized output using key_mapping
for old_key, new_key in key_mapping.items():
    organized_data[new_key] = data.get(old_key, "")

# Save the organized data as a JSON file
with open("output.json", "w") as f:
    json.dump(organized_data, f, indent=4)
