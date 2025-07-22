
# gallerydllm

`gallerydllm` is a command-line tool that uses a Large Language Model (LLM) to convert your natural language instructions into `gallery-dl` commands.

## How it Works


This tool acts as a wrapper around `gallery-dl`, allowing you to describe what you want to do in plain English. `gallerydllm` then uses an LLM to generate the appropriate `gallery-dl` command and executes it for you.

This project defaults to using a local [Ollama](https://ollama.ai/) installation, which allows you to run the LLM on your own machine.

## Installation


1.  **Clone the repository:**
    ```sh
    git clone https://github.com/maxrenke/gallerydllm.git
    cd gallerydllm
    ```


2.  **Install the dependencies:**
    ```sh
    pip install .
    ```

## Usage


To use `gallerydllm`, simply run the command followed by your instructions in quotes:

```sh
gallerydllm "your instructions here"
```

### Configuration


By default, `gallerydllm` connects to a local Ollama instance at `http://localhost:11434/v1` and uses the `llama3:latest` model. You can customize this using the following command-line arguments:

*   `--openai_model`: Specify a different model to use.
*   `--openai_base_url`: Specify a different base URL for the API.


If you want to use the official OpenAI API, you can set the `OPENAI_API_KEY` environment variable and specify the model and base URL accordingly.


### Examples

#### Download All Images from an Album
```sh
gallerydllm "download all images from this Imgur album: <URL>"
```
**Output Command:** `gallery-dl <URL>`

---

#### Download from a Reddit Gallery
```sh
gallerydllm "download all images from this Reddit post: <URL>"
```
**Output Command:** `gallery-dl <URL>`

---

#### Custom Output Directory
```sh
gallerydllm "download all images from <URL> to the folder ./downloads"
```
**Output Command:** `gallery-dl -d ./downloads <URL>`


## Acknowledgements


This project was inspired by and forked from [gstrenge/llmpeg](https://github.com/gstrenge/llmpeg) and based on the ytdlpllm project.

## License

`gallerydllm` is licensed under the MIT License. See the `LICENSE` file for more details.