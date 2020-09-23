# Facebook Automated Comment

Facebook Automated Comment is the open-source project programmed using python3.
[Click Here](https://www.python.org/downloads/), if you don't have python3 installed on your device.

To check whether you have python3 installed on your device, open cmd or terminal and type following command.
```bash
python --version
```

If you get Python 3.x.x, you are good with the installation, if it doesn't work follow the [guide](https://realpython.com/installing-python/).

To get this work, you need to have google-chrome installed on your device so, if you don't have it installed on your device [Click Here](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en)

<br>

## Linux and MacOS Installation

Open your terminal and run the following command:

1. If you don't have git installed:
    #### Debian / Ubuntu
    ```bash
    sudo apt install git-all
    ```

    #### Arch
    ```bash
    sudo pacman -S git-all
    ```

    #### Fedora
    ```bash
    sudo dnf install git-all
    ```

    #### MacOS
    Install [homebrew](https://brew.sh/) if you haven't already.
    ```bash
    brew install git
    ```

2. After you have git and python3 installed, next step is cloning the project.

    ```bash
    git clone https://github.com/h3ck-samrat/FacebookAutomatedComment.git
    ```

3. Navigating to the project.

    ```bash
    cd FacebookAutomatedComment/
    ```

4. Create a new virtual environment to avoid packages conflict and run the file.
    ```bash
    python -m venv commentAutomation
    source /commentAutomation/bin/activate
    pip install -r requirements.txt
    ```

    ```bash
    python3 main.py
    ```

<br>

## Windows Installation

Setup git using this [blog](https://dev.to/qm3ster/setting-up-gitsshgpg-on-windows-5c85) by Mihail Malo.

1. After you have git and python3 installed, next step is cloning the project.

    ```powershell
    git clone https://github.com/h3ck-samrat/FacebookAutomatedComment.git
    ```

2. Navigating to the project.

    ```powershell
    cd FacebookAutomatedComment/
    ```

3. Create a new virtual environment to avoid packages conflict and run the file.
    ```powershell
    python -m venv commentAutomation
    source /commentAutomation/bin/activate
    pip install -r requirements.txt
    ```
    
    ```powershell
    python3 main.py
    ```

Your small contribution may be the biggest contribution to the project. You're welcome for contributing to the project.



