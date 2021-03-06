
import json
import h5py
import numpy as np

######################
## jsonify features ##
######################

# Read the features
def jsonify( h5dataset, saveto, normalize=False ):

  h5f      = h5py.File('vgg_features.h5', 'r')
  features = h5f[ h5dataset ][:]
  h5f.close()

  # Read the filenames
  with open( 'images.csv' ) as f:
    data = f.readlines()

  # Create a dictionary to put the features into
  features_dict = {};

  i = 0;
  for fname in data:
    fname = fname.strip()

    if normalize:
      f = features[:,i];
      f = np.divide( f , np.linalg.norm(f, 2));
      features_dict[ fname ] = f.tolist();
    else:
      features_dict[ fname ] = features[:, i].tolist();
    i = i+1;

  # Save in a json format
  with open( saveto, 'w') as f:
    f.write( json.dumps( features_dict ) );


# === Jsonify image names
with open('images.csv') as f:
  data = f.readlines();

map( (lambda x : x.strip), data );

names = {};
names['names'] =  data;
with open('names.json', 'w') as f:
  f.write( json.dumps( names ));

# === Jsonify features
jsonify( 'features', 'features.json', True );
jsonify( 'embedding', 'embedding.json' );


