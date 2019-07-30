# n_arclogger

Cross-OS ROBLOX shell chat stream deployed via Python 3.7.4

by n_arc

## In-Studio Deployment

Within your chosen game, create a **ModuleScript** in the `Workplace`. Name the modulescript `n_arclogger`.
Create a child **Script** underneath the `n_arclogger` ModuleScript. Name this script `core`.
Open these respective `.lua` files in your download. Paste the corresponding content into the in-game scripts.

Keep in mind that the n_arclogger ModuleScript will need your Discord Webhook URL.

## Discord Integration

Create a random Discord account and create a random server. This ensures security, as all traffic passes through a singular user with different embedded name tags.

Create a new Webhook in the default channel. Default Webhook settings are appropriate.

Copy the Webhook URL and paste it into the 'n_arclogger' ModuleScript in your game.

## Mac Shell Deployment

**Please install the required libraries located within the script.**

Open the `n_arclogger.py` file in your download. Then, navigate to the `# Server Owner User Token` section.

```python
# Server Owner User Token
token = "randomlettersandnumbers.willbe.mixedwithperiods"
```

Replace the `token` value *("randomlettersandnumbers.willbe.mixedwithperiods")* with the user token of the owner of the server in which your logs are hosted. Then, save the file.
Make sure you have Python 3.7.4 installed. All included libraries require this version for functionality.
Find the PATH of the `n_arclogger.py` file.

```shell
/Users/youruser/path/to/file
```

Open Terminal and type in the following command:

```shell
$ python3 /Users/username/path/to/file
```

The stream will open and display the timestamp, username, and message of all chat traffic in the game.

## Windows Shell Deployment

**Please install the required libraries located within the script.**

Open the `n_arclogger.py` file in your download. Then, navigate to the `# Server Owner User Token` section.

```python
# Server Owner User Token
token = "randomlettersandnumbers.willbe.mixedwithperiods"
```

Replace the `token` value *("randomlettersandnumbers.willbe.mixedwithperiods")* with the user token of the owner of the server in which your logs are hosted. Then, save the file.
Make sure you have Python 3.7.4 installed. All included libraries require this version for functionality.
Find the PATH of the `n_arclogger.py` file.

```
C:\Users\username\path\to\file
```

Open CMD and type in the following command:

```
$ python C:\Users\username\path\to\file
```

*Note: You may need to replace* `python` *with the path to your installed python libraries.*

The stream will open and display the timestamp, username, and message of all chat traffic in the game.
