import azure_python_arm_deployer
import json

MAPPING_FILE_NAME = "intent_to_template_mapping.json"

def parse_mapping_file():
    return json.load(open(MAPPING_FILE_NAME))

def deploy_and_confirm(handler_input):
    deployer = azure_python_arm_deployer.ArmTemplateDeployer("ALEXAARMINTEGRATION", "eastus")
    intent_to_template_map = parse_mapping_file()
    try:
        result = deployer.deploy(
            intent_to_template_map[handler_input.request_envelope.request.intent.name][handler_input.request_envelope.request.intent.slots["resourceName"].value]["template_name"])
        print("successful")
        return True
    except Exception as e:
        print(f"Exception is:{e}")
        return False