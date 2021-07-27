 <div align="center">
 <h1> PulseCLI </h1>
 </div>

<p align="center">
:zap: Read stock news in cli :zap:
</p>

## Installation

```console
# clone the repo
$ git clone https://github.com/twentyse7en/pulsecli.git

# change the working directory to sherlock
$ cd pulsecli

# install the requirements
$ pip install .
```

## Usage

```console
$ pulsecli --help

Usage: pulsecli [OPTIONS]

Options:
  -l, --limit INTEGER      limit the number of news. Default: 30
  -s, --style [list|grid]  Output style (list, grid), default is list
  --help                   Show this message and exit.
```

If you are in hurry

```console
$ pulsecli --limit 20 --s grid
```

<p align="center">
<img src="https://user-images.githubusercontent.com/59721339/127202639-7c2ed98d-e000-4ac5-8826-eb528da068bc.png" height=300>
</p>

If you have enough time

```console
$ pulsecli --limit 40
```

<p align="center">
<img src="https://user-images.githubusercontent.com/59721339/127203207-650d4d21-97d9-4bc6-94c1-837d92fd36eb.png" height=300>
</p>

## TODO
- By default it shows trending news, may be an option to select other topics
- Maybe filtering keywords, some news regarding phone lauching are basically ads :p
- Add new style

## Credits
[Pulse](https://pulse.zerodha.com/) for provide news and [starcli](https://github.com/hedyhli/starcli) for layout.

Any contribution, feedback and suggestion are welcome.
