# Section 06: Using non-relational data stores with Hadoop

## Choosing a database technology

Options talked about:
- MySQL 
- MongoDB
- Cassandra
- HBase
- \+ Others

## Integration considerations

- What systems do you need to integrate together?
  - Different technologies have different connectors for different other technologies
    - E.g.: if you have a big analytics job that's currently running in Apache Spark, you probably want to limit yourself to external databases that can connect easily to Apache Spark
  - Or, maybe you have some front-end system that depends on having a SQL interface to a back-end database, and you're thinking about moving from a monolithic relational database to a distributed non-relational database
    - In this case, it might make life a lot easier if the non-relational database you're moving to offers some sort of SQL-like interface that can be easily migrated to and from your front-end application
- So, it is important to think about:
  - The pieces that need to talk together in your system
  - Can they actually talk together or not with existing 'off-the-shelf' components
  - Are those components well maintained and up to date?
- This may already limit your choices then and there

## Scaling requirements
  
- How much data are you dealing with, is it going to grow unbounded over time?
  - If so, then you need some sort of database technology that is not limited to the data that you can store on one PC
  - In this case, you're going to have to look at something like Cassandra, MongoDB or HBase, where you can actually distribute the storage of your data across an entire cluster and scale horizontally instead of vertically
- What will your transaction rates be: how many requests do you expect to get per second?
  - If, for example, this is in the thousands (of requests per second), then again a single database will not be enough
    - You will need something that's distributed where you can spread out the load of those transactions more evenly
    - Typically, in these sorts of situations, we're talking about a big website, where there are lots of web servers serving a lot of people at the same time
    - In these situations, you need to be looking at NoSQL databases more so than monolithic dbs

## Support Considerations

- Do you actually have the in-house expertise to spin up this new technology and actually configure it properly?
  - This will be harder than you think, especially if this is being used in a real-world situation where there may be personally identifiable information in the mix from your end users
  - In this case, it is important to make sure you're thinking very deeply about the security of your system and if the NoSQL dbs covered are configured with default settings, then there'll be **no security at all**.
- Typical scenarios where this might occur include:
  - If you're in a big organisation that has in-house experts to deal with configuration then ok
  - If you're in a smaller organisation:
    - Does this technology offer paid support that will help guide me through setup decisions and initial administration of my server over time?
    - Or are there administrators that I can outsource the ongoing administration over time?
    - For the former, a corporate solution like MongoDB that offers paid support might be a good fit

## Budget considerations? - Probably not.

- Other than cost of support, setup might be relatively cheap
  - Most of Hadoop is open-source
  - Most popular OS for servers is Linux, which is also free
- Costs would include server costs, which can be significant ia large application or distribution

## CAP Considerations

- Which two of consistency, availability and partition-tolerance do you want/need?
  - If scale is important -> partition-tolerance
  - How important is consistency and availability?
    - Availability - is your system going down for a few minutes not acceptable -> availability
    - Consistency - is it unacceptable for users to see delays in updated data or information -> consistency
- Note: these are not hard and fast rules, lines are getting blurred between these trade-offs, e.g. Cassandra

## Simplicity

- Keep it simple, stupid

## Example 1: Phone directory app

- You're building an internal phone directory app
  - Scale: limited (for company employees only)
  - Consistency: Eventual is fine (doesn't have to be instantly updated)
  - Availability requirements: not mission critical (downtimes can be tolerated if not excessive)
  - MySQL/RDBMS is probably already installed on your web server (for storing this employee data)
  - Choice -> **MySQL** (easy, simple, cheap)

## Example 2: Mining web server logs

- You want to mine web server logs for interesting patterns?
  - I.e. what are the most popular times of day, average session length, .., etc
- Is a database even needed for serving data to users?
  - Or can analysis be done offline using Spark and 'dumping' the data in HDFS?
- Choice: **None of the above** - user Hadoop FS

## Example 3: Movie recommendation app

- You have a big Spark job that produces movie recommendations for end users nightly
- Something needs to vend this data to your web applications
- **Scale**: You work for a large company that has a large amount of data
- **Availability**: downtime is not tolerated
- **Performance/Partition-tolerance**: must be fast
- **Consistency**: eventual consistency OK - it just reads
- **Choice**: **Cassandra**

## Exercise: Stock trading system

- You're building a massive stock trading system
  - **Consistency**: is more important than anything
  - **Partition-tolerance**: "Big data" is present
  - **Commercial solution/security**: Really, really important - so having access top professional support might be a good idea and you have the budget to pay for it
  - **Availability**: important but not as much as consistency
  - Choice: **HBase or MongoDB** (latter having more commercial support)
    - These are highly consistent due to only having one master
    - Also partition-tolerant
    - Due to commercial support criteria -> MongoDB, unless there is a company that has strong HBase support -- do your research!