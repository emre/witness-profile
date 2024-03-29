# witness-profile

A personal page app for STEEM witnesses.

# Installation

```
$ python3.6 -m venv witness-profile-env
$ source witness-profile-env/bin/activate
$ git clone https://github.com/emre/witness-profile.git      
$ cd witness-profile
$ pip install -r requirements.txt
```

# Configuration

witness-profile doesn't use any database. All you need to do is creating a file
in your path. (Ex: profile.json)

```json
{
  "witness_account": "emrebeyler",
  "witness_name": "emrebeyler",
  "witness_title": "Developer, STEEM Witness, Creator of dpoll.xyz",
  "witness_description": "I am an experienced software developer in Istanbul/Turkey. \n\nI am passionate about the STEEM blockchain. Supporting the network by maintaining a witness node and developing countless applications/tools around it.",
  "servers": [
    {"name": "Primary", "ram": "64 GB DDR4", "bw": "1 GBit/s", "cpu": "Intel i7-6700 Quad-Core", "hdd": "2x2 TB SATA HDD 7200 RPM "}
  ],
  "projects": [
    {
      "name": "dpoll",
      "description": "dpoll.xyz is an experimental application on the top of the STEEM blockchain. It has an account based voting system, where accounts may vote specific questions asked by other STEEM accounts.",
      "url": "https://dpoll.xyz",
      "github_repo": "https://github.com/emre/dpoll.xyz",
      "logo": "https://i.postimg.cc/BvW7cZX3/dpoll-logo.png"
    },
    {
      "name": "lightsteem",
      "description": "Lightsteem is a light python client to interact with the STEEM blockchain. It’s simple and stupid. It doesn’t interfere the process between the developer and the STEEM node.",
      "github_repo": "https://github.com/emre/lightsteem",
      "logo": "https://i.postimg.cc/BbM73xSc/lightsteem-logo.png",
      "url": "https://lightsteem.readthedocs.io/en/latest/"
    },
    {
      "name": "steemconnect-python-client",
      "description": "steemconnect-python-client is a simple yet powerful library to interact with the Steemconnect. Steemconnect is a central-single sign on solution for steem based applications.",
      "url": "https://steemconnect-python-client.readthedocs.io/en/latest/",
      "github_repo": "https://github.com/emre/steemconnect-python-client"
    },
    {
      "name": "transmitter",
      "description": "Transmitter is a CLI tool for STEEM blockchain witnesses. It quickly allows you to enable/disable your witness or set some properties for the new witness_set_properties call introduced in Hard Fork 20.",
      "github_repo": "https://github.com/emre/transmitter",
      "logo": "https://i.postimg.cc/y8NnmgV2/transmitter-logo.png"
    },
    {
      "name": "infestor",
      "description": "infestor is a cross platform CLI app to claim and create discounted accounts on the STEEM blockchain.",
      "github_repo": "https://github.com/emre/infestor",
      "logo": "https://i.postimg.cc/mrBLpsnx/infestor-logo.png"
    }
  ],
  "delegations": [
    {
      "account": "dpoll.curation",
      "amount": 2500
    },
    {
      "account": "sndbox",
      "amount": 100
    },
    {
      "account": "steemflagrewards",
      "amount": 100
    },
    {
      "account": "partiko",
      "amount": 100
    },
    {
      "account": "edebiyat",
      "amount": 100
    }
  ],
  "social_ids": {
    "github": "emre",
    "discord": "emrebeyler#9263"
  },
  "community_involvements": [
    {
      "name": "Sndbox",
      "account": "sndbox",
      "website": "https://sndbox.co/",
      "title": "Steward",
      "description": "I help @sndbox as a curator for organized contests. Also maintain the main discord bot handles registration and curation."
    },
    {
      "name": "The Creative Crypto",
      "account": "creativecrypto",
      "website": "https://thecreativecrypto.com",
      "title": "Developer",
      "description": "I develop and maintain an automated voting bot for the creative content in the STEEM blockchain."
    },
    {
      "name": "Utopian",
      "account": "utopian-io",
      "website": "https://utopian.io",
      "title": "Moderator",
      "description": "I review submissions in the development category."
    }
  ]
}
```

After creating the file, edit ```config.py``` in the project and set ```WITNESS_PROFILE_JSON_FILE"``` variable with your profile.json file's path.


# Running

in the project's directory:

```
$ gunicorn app:app
```

This will start listening on port 8000. You can deploy it via [nginx](http://docs.gunicorn.org/en/stable/deploy.html) and proxy pass your 80.port to 8000.
