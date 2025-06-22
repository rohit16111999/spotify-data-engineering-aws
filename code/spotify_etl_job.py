import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node tracks
tracks_node1745218564312 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-spotify-analysis-1/staging/track.csv"], "recurse": True}, transformation_ctx="tracks_node1745218564312")

# Script generated for node artist
artist_node1745218563075 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-spotify-analysis-1/staging/artists.csv"], "recurse": True}, transformation_ctx="artist_node1745218563075")

# Script generated for node album
album_node1745218563695 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-spotify-analysis-1/staging/albums.csv"], "recurse": True}, transformation_ctx="album_node1745218563695")

# Script generated for node Join Album & Artist
JoinAlbumArtist_node1745218733288 = Join.apply(frame1=album_node1745218563695, frame2=artist_node1745218563075, keys1=["artist_id"], keys2=["id"], transformation_ctx="JoinAlbumArtist_node1745218733288")

# Script generated for node Join with tracks
Joinwithtracks_node1745218929624 = Join.apply(frame1=tracks_node1745218564312, frame2=JoinAlbumArtist_node1745218733288, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Joinwithtracks_node1745218929624")

# Script generated for node Drop Fields
DropFields_node1745219004928 = DropFields.apply(frame=Joinwithtracks_node1745218929624, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1745219004928")

# Script generated for node Destination
EvaluateDataQuality().process_rows(frame=DropFields_node1745219004928, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1745218522214", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Destination_node1745219061576 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1745219004928, connection_type="s3", format="glueparquet", connection_options={"path": "s3://project-spotify-analysis-1/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1745219061576")

job.commit()