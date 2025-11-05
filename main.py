from pyscript import display, document

def general_weighted_average(e):
    subjects = ['Astronomy', 'Potions', 'Charms', 'Transfigurations', 
                'Flying', 'Herbology', 'History of Magic', 'Defense Against the Dark Arts']
    units = [5, 5, 5, 3, 2, 1, 2, 1]

    # Get student info
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value
    house_name = document.getElementById('house_name').value

    # Get grades
    grades = [
        float(document.getElementById('astronomy').value),
        float(document.getElementById('potions').value),
        float(document.getElementById('charms').value),
        float(document.getElementById('transfigurations').value),
        float(document.getElementById('flying').value),
        float(document.getElementById('herbology').value),
        float(document.getElementById('history_of_magic').value),
        float(document.getElementById('dada').value)
    ]

    # Compute weighted average
    # g is grade, u is unit
    weighted_sum = sum(g * u for g, u in zip(grades, units))
    total_units = sum(units)
    gwa = weighted_sum / total_units

    # Display info
    student_info = f"🧙‍♂️ {first_name} {last_name}\n🏰 House: {house_name}\n✨ GWA: {gwa:.2f}"
    summary = "\n".join(f"{s}: {g}" for s, g in zip(subjects, grades))

    display(student_info, target="student_info")
    display(summary, target="summary")
