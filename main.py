from pyscript import document

clubs = {
    "Chess Club": {
        "description": "A club for chess enthusiasts of all skill levels.",
        "meeting_time": "Every Wednesday 3:30-5:00 PM",
        "location": "Room 405",
        "advisor": "Mr. Santos",
        "members": 20,
        "category": "Academic"
    },
    "Science Club": {
        "description": "Encourages scientific exploration and experiments.",
        "meeting_time": "Friday 3:00-4:30 PM",
        "location": "Science Lab",
        "advisor": "Ms. Cruz",
        "members": 25,
        "category": "Academic"
    }
}

def show_club_info(event):
    selected_club = document.getElementById("club-select").value
    club = clubs[selected_club]

    output = (
        f"{selected_club}\n"
        f"Description: {club['description']}\n"
        f"Meeting Time: {club['meeting_time']}\n"
        f"Location: {club['location']}\n"
        f"Advisor: {club['advisor']}\n"
        f"Number of Members: {club['members']}\n"
        f"Category: {club['category']}"
    )

    document.getElementById("result").innerText = output

document.getElementById("show-btn").addEventListener("click", show_club_info)
