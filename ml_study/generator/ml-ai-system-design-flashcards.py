import pandas as pd
import random

def generate_flashcards():
    """
    Generate a comprehensive set of flashcards for ML, AI, and System Design
    """
    flashcards = []
    
    # Machine Learning Flashcards
    ml_questions = [
        ("What is overfitting in machine learning?", "Overfitting occurs when a model learns the training data too closely, including its noise and fluctuations, leading to poor generalization on new, unseen data."),
        ("Explain the bias-variance tradeoff", "The bias-variance tradeoff is a fundamental concept in machine learning where decreasing bias increases variance, and vice versa. Optimal models balance these two sources of error."),
        ("What is gradient descent?", "Gradient descent is an optimization algorithm used to minimize the cost function by iteratively moving in the direction of steepest descent, helping machine learning models find optimal parameters."),
        ("Define precision and recall", "Precision is the ratio of true positive predictions to total positive predictions. Recall is the ratio of true positive predictions to total actual positive instances."),
        ("What is cross-validation?", "Cross-validation is a technique to assess a model's performance by dividing the data into subsets, training on some and validating on others to ensure the model generalizes well."),
        ("Explain the difference between supervised and unsupervised learning", "Supervised learning uses labeled data to train models, while unsupervised learning finds patterns in unlabeled data without predefined categories."),
        ("What is regularization?", "Regularization is a technique to prevent overfitting by adding a penalty term to the loss function, discouraging complex models and promoting simpler, more generalizable solutions."),
        ("Define entropy in machine learning", "Entropy measures the impurity or randomness in a dataset. In decision trees, it helps determine the best splits by choosing features that reduce uncertainty."),
        ("What are ensemble methods?", "Ensemble methods combine multiple machine learning models to create a more robust and accurate predictive model, such as random forests or gradient boosting."),
        ("Explain the concept of feature scaling", "Feature scaling normalizes the range of independent variables to ensure all features contribute equally to model training, preventing features with larger magnitudes from dominating.")
    ]
    
    # AI Flashcards
    ai_questions = [
        ("What is the Turing Test?", "The Turing Test, proposed by Alan Turing, evaluates a machine's ability to exhibit intelligent behavior indistinguishable from a human, typically through conversational interaction."),
        ("Define Natural Language Processing (NLP)", "Natural Language Processing is a branch of AI that focuses on the interaction between computers and human language, enabling machines to understand, interpret, and generate human language."),
        ("What are neural networks?", "Neural networks are computing systems inspired by biological neural networks, consisting of interconnected nodes (neurons) that process and transmit information, fundamental to deep learning."),
        ("Explain the difference between AI, Machine Learning, and Deep Learning", "AI is the broader concept of machines being able to carry out tasks intelligently. Machine Learning is a subset of AI using statistical techniques. Deep Learning is a subset of Machine Learning using neural networks with multiple layers."),
        ("What is the Turing Completeness of AI?", "Turing Completeness refers to a system's ability to simulate a Turing machine, meaning it can perform any computational task given enough time and memory."),
        ("Define generative AI", "Generative AI refers to artificial intelligence systems that can create new content, including text, images, audio, and video, by learning patterns from existing data."),
        ("What is transfer learning?", "Transfer learning is an AI technique where a model developed for one task is reused as the starting point for a model on a second, related task, reducing training time and improving performance."),
        ("Explain reinforcement learning", "Reinforcement learning is an AI approach where an agent learns to make decisions by performing actions in an environment and receiving rewards or penalties."),
        ("What are transformer models?", "Transformer models are a type of neural network architecture using self-attention mechanisms, enabling more efficient processing of sequential data, particularly successful in NLP tasks."),
        ("Define explainable AI (XAI)", "Explainable AI focuses on creating machine learning models whose actions can be easily understood by humans, addressing the 'black box' problem in complex AI systems.")
    ]
    
    # System Design Flashcards
    system_design_questions = [
        ("What is horizontal scaling?", "Horizontal scaling (scaling out) involves adding more machines to a system to distribute the load, increasing overall capacity and performance by adding more nodes to a network."),
        ("Explain the CAP theorem", "The CAP theorem states that a distributed computer system can only simultaneously provide two out of three guarantees: Consistency, Availability, and Partition tolerance."),
        ("What is microservices architecture?", "Microservices architecture is an approach where an application is built as a collection of small, independent services that communicate through APIs, enabling easier maintenance and scalability."),
        ("Define load balancing", "Load balancing distributes network traffic across multiple servers to ensure no single server bears too much demand, improving responsiveness and availability of applications."),
        ("What is a distributed cache?", "A distributed cache is a caching system spread across multiple servers, improving data retrieval speed and reducing the load on primary data stores."),
        ("Explain eventual consistency", "Eventual consistency is a consistency model where updates to a distributed system will propagate eventually, allowing temporary inconsistencies but guaranteeing that all replicas will converge."),
        ("What is a message queue?", "A message queue is a middleware that enables asynchronous communication between different parts of a distributed system, decoupling components and improving system reliability."),
        ("Define sharding in databases", "Sharding is a database partitioning technique that splits large databases into smaller, more manageable pieces called shards, distributed across multiple servers."),
        ("What is a service-oriented architecture (SOA)?", "Service-oriented architecture is a design approach where application components provide services to other components via a communication protocol over a network."),
        ("Explain the concept of rate limiting", "Rate limiting is a technique to control the rate of traffic sent or received on a network interface controller, preventing abuse and ensuring fair resource allocation.")
    ]
    
    # Combine and randomize questions
    all_questions = ml_questions + ai_questions + system_design_questions
    
    # Generate 100 entries with random selection and categorization
    for _ in range(100):
        question, answer = random.choice(all_questions)
        
        # Categorize based on origin
        if (question, answer) in ml_questions:
            category = "Machine Learning"
        elif (question, answer) in ai_questions:
            category = "Artificial Intelligence"
        else:
            category = "System Design"
        
        flashcards.append({
            "question": question,
            "answer": answer,
            "category": category
        })
    
    return flashcards

# Generate and save flashcards
flashcards_data = generate_flashcards()
df = pd.DataFrame(flashcards_data)

# Save to CSV with proper quoting
df.to_csv('ml_ai_system_design_flashcards.csv', index=False, quoting=1)

print("CSV file generated successfully!")
print("\nSample of generated flashcards:")
print(df.head())
print(f"\nTotal entries: {len(df)}")
print("\nCategory Distribution:")
print(df['category'].value_counts())
