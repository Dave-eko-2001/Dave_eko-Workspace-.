def calculate_velocity(displacement, time):
    if time <= 0:
        raise ValueError("Time must be greater than zero.")
    return displacement / time


def calculate_momentum(mass, velocity):
    return mass * velocity


def calculate_pressure(force, area):
    if area <= 0:
        raise ValueError("Area must be greater than zero.")
    return force / area


def calculate_impulse(force, time):
    return force * time


def calculate_force(mass, acceleration):
    return mass * acceleration


def physics_questions():
    print("Physics Quiz! Answer the following questions.")

    try:
        # Question 1: Velocity
        print("\n1. A car travels 100 meters in 5 seconds. What is its velocity?")
        user_answer = float(input("Your answer (in m/s): "))
        correct_answer = calculate_velocity(100, 5)
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer:.2f} m/s.")
            print("Working: Velocity = Displacement / Time = 100 / 5 = 20 m/s.")

        # Question 2: Momentum
        print("\n2. A 10 kg object moves at 3 m/s. What is its momentum?")
        user_answer = float(input("Your answer (in kg*m/s): "))
        correct_answer = calculate_momentum(10, 3)
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer:.2f} kg*m/s.")
            print("Working: Momentum = Mass * Velocity = 10 * 3 = 30 kg*m/s.")

        # Question 3: Pressure
        print("\n3. A force of 50 N is applied over an area of 2 m². What is the pressure?")
        user_answer = float(input("Your answer (in Pa): "))
        correct_answer = calculate_pressure(50, 2)
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer:.2f} Pa.")
            print("Working: Pressure = Force / Area = 50 / 2 = 25 Pa.")

        # Question 4: Impulse
        print("\n4. A force of 10 N acts for 2 seconds. What is the impulse?")
        user_answer = float(input("Your answer (in Ns): "))
        correct_answer = calculate_impulse(10, 2)
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer:.2f} Ns.")
            print("Working: Impulse = Force * Time = 10 * 2 = 20 Ns.")

        # Question 5: Force
        print("\n5. A mass of 5 kg accelerates at 2 m/s². What is the force acting on it?")
        user_answer = float(input("Your answer (in N): "))
        correct_answer = calculate_force(5, 2)
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer:.2f} N.")
            print("Working: Force = Mass * Acceleration = 5 * 2 = 10 N.")

    except ValueError as e:
        print(f"Error: {e}")


# Call the function to run the quiz
physics_questions()


