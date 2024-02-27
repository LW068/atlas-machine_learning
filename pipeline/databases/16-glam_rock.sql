-- Lists all bands with Glam rock as their main style, ranked by their longevity
SELECT name AS band_name, IF(split='-', 2020 - formed, split - formed) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam Rock'
ORDER BY lifespan DESC;