import click
import cligj
import json

from geojson_precision import coord_precision as process_features


@click.command()
@cligj.features_in_arg
@cligj.sequence_opt
@cligj.use_rs_opt
@click.option("--precision", '-p', type=int, default=6,
              help="number of decimal places for coordinate positions")
def main(features, sequence, use_rs, precision):
    if sequence:
        for feature in process_features(features, precision):
            if use_rs:
                click.echo(u'\x1e', nl=False)
            click.echo(json.dumps(feature))
    else:
        click.echo(json.dumps(
            {'type': 'FeatureCollection',
             'features': list(process_features(features, precision))}))
