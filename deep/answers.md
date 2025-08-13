# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning
Reasons for taking this approach would be the fast way of sending data to the surface because there would not be a single queue or channel to send the data, so the data can be captured more quickly. So ingesting the data would be fast. Also, all resources, meaning boats, would be used so no money wasted. The problem is when you want to select a particular record because the data is spread out with the same probability to land on a particular boat (for 3 boats the chance of being stored in a boat is 1/3), so to find a record you have to read the data from all the boats. So reading the data would take more time and it would consume for resources.

## Partitioning by Hour

Reasons for taking this approach would be the maximization of storage usage, because of the timeframe, one of the boats
can get most of the observations. So as long as you know which boat has the data for a particular timeframe, that should be fine. The downside
is that some boats or storages would be empty or idle and you might end up wasting money on resources you don't use. The good thing is that
querying the data would be fast and efficient because that data would be concentrated in one or fewer boats.

## Partitioning by Hash Value

A good reason to use this approach is the use of all available storages or boats similar to the partitioning method because each boat can
support a range of hash values, and depending of the timestamp, a record can land in anyone of the boats with the same chance. With regard
to reading data, if you select all the records you have to query all the boats but if you want a particular record, this can be done more
quickly because by getting the hash value of the timestamp, you can identify which boat has the range of hash values containing the hash
value you are looking for. So reading data would be more efficient.
