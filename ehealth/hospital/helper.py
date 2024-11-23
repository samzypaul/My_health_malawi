import uuid

def generate_subscription_code(doctor):
    # Generate a unique code tied to the doctor
    return f"{doctor.id}-{uuid.uuid4().hex[:8]}"
