-- Lists all bands with Glam rock as their main style, ranked by their longevity
SELECT name AS band_name, (IF(split = '0', 2020, split) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
