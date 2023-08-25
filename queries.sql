-- queries.sql
-- Highest performing ads with non-zero CTR
SELECT c.id, m.media_id, m.asset_url, c.ad_url,
       p.impressions, p.clicks, p.conversions,
       p.ctr, p.cost_per_ad_click, p.cpc, p.cpm
FROM campaigns c
INNER JOIN media m ON c.id = m.campaigns_id
INNER JOIN performance_data p ON c.id = p.campaign_id
WHERE c.advertiser_id = 28
AND p.ctr > 0
ORDER BY p.ctr DESC
LIMIT 10;

-- Other queries...
