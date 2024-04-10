# TextToSpeechNow

TextToSpeechNow is a Python-based tool designed to convert text into speech using either Google's Text-to-Speech (gTTS) or OpenAI's text-to-speech models. This flexible and easy-to-use tool supports multiple languages and offers a choice of voices, making it suitable for a wide range of text-to-speech applications.

## Features
- **Google's Text-to-Speech**: Leverage the power and versatility of Google's Text-to-Speech engine.
- **OpenAI's Text-to-Speech**: Utilize OpenAI's advanced text-to-speech models for high-quality speech synthesis.
- **Ease of Integration**: Designed for easy integration into Python applications, making it straightforward to add text-to-speech capabilities to your projects.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or higher

Additionally, you will need:

- An API key from OpenAI if you intend to use OpenAI's text-to-speech models.

## Installation
To get started with TextToSpeechNow, follow these steps:

Clone the repository:
```sh
git clone https://github.com/bpgatchalian/TextToSpeechNow.git
```
Navigate to the project directory:
```sh
cd TextToSpeechNow
```
Install the required Python packages:
```sh
pip install -r requirements.txt
```

## Setting Up Environment Variables
You need to set your OpenAI API key as an environment variable. Create a .env file in the project directory and add your API key as follows:

```makefile
OPENAI_API_KEY=your_api_key_here
```

## Usage
TextToSpeechNow offers two main functionalities: playing text-to-speech audio directly through your speakers and saving the synthesized speech as an audio file. Below are examples of how to use both.

### Playing Text-to-Speech Audio
To play text-to-speech audio directly, use the speak method. This method synthesizes the text into speech and plays the audio immediately:

```python
tts_now = TextToSpeechNow()
tts_now.speak("Hello, welcome to TextToSpeechNow.")
```

### Saving Synthesized Speech as an Audio File
If you prefer to save the synthesized speech as an audio file for later use, use the synthesize_text method. This allows you to specify an output path for the audio file:

```python
tts_now = TextToSpeechNow()
tts_now.synthesize_text("Hello, welcome to TextToSpeechNow.", output_path="output.mp3")
```
This method is particularly useful when you need to generate speech audio files for use in applications, presentations, or any other scenario where the audio is required to be played back at a later time.

## Configuration
TextToSpeechNow allows customization at both initialization and method invocation levels, providing flexibility for different use cases. Here's how you can configure its behavior:

### Initialization Parameters
Customize TextToSpeechNow's behavior by modifying the following parameters when instantiating the TextToSpeechNow class:

- **tts_engine**: Choose the text-to-speech engine ("google_tts" for Google's Text-to-Speech or "openai_tts" for OpenAI's text-to-speech models). Default: "google_tts".
- **language**: Set the language of the text-to-speech output using ISO language codes (e.g., "en", "es"). Default: "en".
- **model**: (OpenAI's text-to-speech only) Specify the model for speech synthesis. Default: "tts-1".
- **voice**: (OpenAI's text-to-speech only) Select the voice for the output. Default: "nova".
```python
tts_now = TextToSpeechNow(
    tts_engine="openai_tts",
    language="en",
    model="tts-1",
    voice="nova"
)
```

### Method Parameters

#### speak(text)
Plays the synthesized speech audio directly.

- **text**: The text to be converted into speech.

```python
tts_now.speak("Hello, welcome to TextToSpeechNow.")
```

#### synthesize_text(text, output_path)
Converts text to speech and saves the output as an audio file.

- **text**: The text to be converted into speech.
- **output_path**: The file path where the audio file will be saved. Include the file name and extension (e.g., "output.mp3").

```python
tts_now.synthesize_text("Hello, welcome to TextToSpeechNow.", output_path="output.mp3")
```

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.