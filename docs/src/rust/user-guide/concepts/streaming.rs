use polars::prelude::*;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // --8<-- [start:query]
    let q = LazyCsvReader::new("docs/data/iris.csv")
        .has_header(true)
        .finish()?
        .filter(col("sepal_length").gt(lit(5)))
        .group_by(vec![col("species")])
        .agg([col("sepal_width").mean()]);
    // --8<-- [end:query]
    # --8<-- [start:streaming_query_plan]
    plan = q.with_streaming(true).describe_plan();
    println!("{}", plan);

    # --8<-- [end:streaming_query_plan]
    
    // --8<-- [start:streaming]

    let df = q.with_streaming(true).collect()?;
    println!("{}", df);
    // --8<-- [end:streaming]

    Ok(())
}
