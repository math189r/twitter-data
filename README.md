### `twitter-data`
#### Collects tweets from the streaming API.

The repository includes a dataset of 1.4 Million tweets partitioned by sentiment using this functionality.

### Usage

```bash
$ python3 run.py --config example_config.json
```

Most functionality is defined within the config file. See the example config for details on the options. Basically you can either use the sample endpoint _or_ the filter endpoint with filters on the content of the tweets you pull.

If you want the data in its own file, just pipe the output into a file eg.
```bash
$ python3 run.py --config example_config.json > output_data.json
```
