import os
import subprocess

vehicle_labels = [
    'Car', 'Truck', 'Vehicle', 'Bus', 'Bicycle', 'Motorcycle',
    'Excavator', 'Bulldozer', 'Crane', 'Dump Truck', 'Forklift',
    'Backhoe', 'Loader', 'Concrete Mixer', 'Tractor', 'Grader',
    'Scraper', 'Skid-Steer Loader', 'Paver', 'Compactor',
    'Telehandler', 'Scissor Lift', 'Boom Lift', 'Road Roller',
    'Pile Driver', 'Drilling Machine', 'Asphalt Paver', 'Hydraulic Hammer',
    'Mixer Truck', 'Articulated Dump Truck', 'Mini Excavator',
    'Wheel Loader', 'Crawler Loader', 'Track Loader', 'Trencher'
]

people_labels = [
    "Person", "Pedestrian", "Worker", "Cyclist", "Motorcyclist",
    "Construction Worker", "Traffic Officer", "Security Guard",
    "Police Officer", "Emergency Responder", "Paramedic",
    "Engineer", "Supervisor", "Foreman", "Surveyor", "Electrician",
    "Plumber", "Welder", "Architect", "Inspector", "Site Manager",
    "Mason", "Painter", "Heavy Equipment Operator", "Flagger",
    "Rigger", "Steel Worker", "Concrete Worker", "Crane Operator"
]

violation_labels = [
    "Helmet Violation", "Seatbelt Violation", "Speeding",
    "Unauthorized Access", "Restricted Area Violation",
    "Jaywalking", "Running Red Light", "Overloaded Vehicle",
    "Illegal Parking", "Failure to Yield", "Driving Against Traffic",
    "No Helmet", "No Safety Vest", "Using Phone While Driving",
    "Unsafe Equipment Use", "Failure to Signal", "DUI",
    "No Gloves", "No Goggles", "No Ear Protection", "No Face Mask",
    "Unsafe Ladder Use", "Blocked Emergency Exit", "Unstable Scaffolding",
    "Unauthorized Machinery Use", "Improper Lifting Technique",
    "Falling Object Hazard", "Electrical Hazard", "Gas Leak",
    "No Fire Extinguisher", "No Safety Harness", "Faulty Equipment",
    "Improper Material Storage", "Oil Spill", "Unsecured Load",
    "Exceeding Noise Limit", "Inadequate Lighting", "Poor Ventilation"
]

safety_gear_labels = [
    "Helmet", "Safety Vest", "Gloves", "Safety Goggles",
    "Face Shield", "Ear Protection", "Respirator Mask",
    "Steel-Toe Boots", "Harness", "Knee Pads", "Reflective Strips"
]

site_condition_labels = [
    "Dust Cloud", "Wet Surface", "Slippery Floor", "Pothole",
    "Loose Wires", "Smoke", "Fog", "Falling Debris",
    "Heavy Rain", "Mud", "Snow", "Strong Winds"
]

equipment_labels = [
    "Scaffolding", "Ladder", "Cement Bag", "Bricks", "Rebar",
    "Wood Planks", "Concrete Slab", "Steel Beams", "Pipes",
    "Electrical Cables", "Welding Machine", "Jackhammer",
    "Chainsaw", "Drill", "Circular Saw", "Hammer", "Wrench",
    "Screwdriver", "Measuring Tape", "Safety Cone", "Barricade",
    "Caution Tape", "First Aid Kit", "Fire Extinguisher",
    "Work Light", "Portable Generator", "Toolbox"
]

def create_folders(root_name, labels):
    os.makedirs(root_name, exist_ok=True)
    for label in labels:
        folder_name = label.replace(" ", "_")
        os.makedirs(os.path.join(root_name, folder_name), exist_ok=True)

def run_git_commands(branch):
    # Checkout to feature branch
    subprocess.run(["git", "checkout", branch], check=True)
    # Add changes
    subprocess.run(["git", "add", "."], check=True)
    # Commit changes
    subprocess.run(["git", "commit", "-m", f"Added folder structure under {branch} branch"], check=True)
    # Push changes to remote repository
    subprocess.run(["git", "push", "origin", branch], check=True)
    print(f"Changes pushed to branch '{branch}' successfully.")

if __name__ == "__main__":
    create_folders("vehicle_labels", vehicle_labels)
    create_folders("people_labels", people_labels)
    create_folders("violation_labels", violation_labels)
    create_folders("safety_gear_labels", safety_gear_labels)
    create_folders("site_condition_labels", site_condition_labels)
    create_folders("equipment_labels", equipment_labels)

    feature = "feature"  # Change this to your actual branch name
    run_git_commands(feature)
