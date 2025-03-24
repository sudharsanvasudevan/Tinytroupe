from tinytroupe import Person  # Replace 'Person' with the correct class name

# Define a persona
lisa = Person(
    name="Lisa",
    age=30,
    nationality="Canadian",
    occupation="Data Scientist",
    professional_history="Lisa has been working in AI and ML for 5 years."
)

# Interact with the persona
response = lisa.listen_and_act("Tell me about your life.")
print(response)
