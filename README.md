# AI Chatbot – Multi-Personality Conversational Assistant

An intelligent conversational AI chatbot powered by DeepSeek-R1 from Hugging Face. This application enables dynamic, context-aware conversations with multiple personality modes tailored to different use cases.

---

## Features

### Multiple Personality Modes

Choose from 8 distinct assistant behaviors:

* Funny – Humorous and entertaining responses
* Professional – Formal and business-oriented communication
* Sarcastic – Witty and sharp responses
* Friendly – Warm and approachable tone
* Helpful – Direct and solution-focused
* Expert – Technical and detailed explanations
* Wise – Thoughtful and philosophical responses
* Creative – Imaginative and unconventional thinking

---

### Core Capabilities

* Natural Language Understanding using DeepSeek-R1
* Context-aware conversations with memory of prior messages
* Multi-turn dialogue support
* Real-time response generation
* Adaptive tone based on selected personality

---

## Technology Stack

| Layer    | Technology                 |
| -------- | -------------------------- |
| AI Model | DeepSeek-R1 (Hugging Face) |
| NLP      | Hugging Face Transformers  |
| Backend  | Python                     |
| Frontend | Streamlit                  |

---

## Screenshots

### Bot Mode Selection

Select a personality mode for the chatbot:

![Bot Mode](https://github.com/mahaveer116/chatbot-/blob/a152c6e55ca6ca8334c70125e334cd782faa6a0c/options.png)

---

### Chat Interface

Simple and intuitive interface for interacting with the chatbot:

![Chat Interface](https://github.com/mahaveer116/chatbot-/blob/a152c6e55ca6ca8334c70125e334cd782faa6a0c/chatinterface%20.png)

---

## How It Works

```mermaid
flowchart LR
    A[Select Personality] --> B[User Input]
    B --> C[Process via Transformer]
    C --> D[Maintain Context]
    D --> E[Generate Response]
    E --> F[Display in UI]
```

1. User selects a personality mode
2. Input message is processed through the transformer model
3. Conversation history is maintained for context
4. DeepSeek-R1 generates a response based on tone and context
5. Output is displayed in real time

---

## Use Cases

* Customer support automation
* Educational assistance
* Creative writing support
* Technical problem solving
* General conversation
* Professional communication

---

## Key Highlights

* Transformer-based architecture
* Optimized for low-latency responses
* Efficient context management
* Robust error handling

---

## Future Enhancements

* Voice input and output
* Multi-language support
* Custom personality creation
* Chat history export
* Integration with external knowledge sources
* Advanced memory and personalization
* Domain-specific fine-tuning

---

## Model Information

This chatbot leverages the DeepSeek-R1 model, which provides:

* Strong natural language understanding
* Context-aware response generation
* Multi-turn conversation capability
* Efficient inference performance

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a pull request

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

* Hugging Face Transformers
* DeepSeek-R1 model
* Streamlit
