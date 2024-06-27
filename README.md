# atlas-talk
MongoDB Atlas CLI interactive help

## prerequisites
- python 3
- poetry

## running

1. setup a `.env` file based on examples on `env` folder
2. run `make prepare` to prepare data
3. run `make start` to run web server
4. run `make chat` to start

## use cases

- chatbot for getting help in atlas cli command (e.g. `atlas assist` or `atlas talk`)
- chatbot for getting help inside of atlas ui (ideally we could add a screen context)
- add more context to chatbot (understanding of clusters, data federation, etc)

## challenges

- authentication: to know your orgs, projects, clusters and more we need to figure out auth between backend and apis
- evaluation: while bringing more functionality is key also measuring level of feedback is key to improve level of efficiency

## value
- ai experience to help with adoption, troubleshooting and self help
