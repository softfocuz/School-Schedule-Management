from data import timeslots, subjects7_sectionA, subjects7_sectionB, subjects7_sectionC

sections = ["7A", "7B", "7C"]
schedules = {section: {} for section in sections}

for section in sections:
    for slot in timeslots:
        key = f"{slot['day']} {slot['time']}"
        if slot["time"] == "12:00-13:00":
            schedules[section][key] = "LUNCH"
        else:
            schedules[section][key] = None

teachers = {}
for t in range(1, 12 + 1):
    teachers[t] = set()

def assign_subjects(section, subjects):
    for subject in subjects:
        hours = subject["hours"]
        teacher_id = subject["teacher_id"]
        used_days = set()

        for slot in timeslots:
            day = slot["day"]
            key = f"{day} {slot['time']}"

            if hours == 0:
                break

            if schedules[section][key] is not None or day in used_days:
                continue

            if key in teachers[teacher_id]:
                continue

            schedules[section][key] = subject["name"]
            teachers[teacher_id].add(key)
            used_days.add(day)
            hours -= 1

assign_subjects("7A", subjects7_sectionA)
assign_subjects("7B", subjects7_sectionB)
assign_subjects("7C", subjects7_sectionC)

for section in sections:
    print(f"\nSCHEDULE FOR SECTION {section}")
    for key, value in schedules[section].items():
        print(f"{key} : {value}")
