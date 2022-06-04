# Anki backlog management add-on.

## install

## config

## usage

# Development

I do development in a folder outside of Anki AddOns, and then I "deploy" (copy) the code to the addons folder.

To do so (at least on a Mac):

```
cd deploy/
cp deploy.config.example deploy.config
# ... now edit deploy/deploy.config for your system
cd ..
```

Run the deployment script from root:

```
$ ./deploy/deploy.sh
```