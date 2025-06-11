sql_queries = [
    ("1. Total food listings by provider type", 
     '''SELECT provider_type, COUNT(*) AS total_listings FROM foodlistings GROUP BY provider_type;'''),

    ("2. Total food quantity by food type", 
     '''SELECT food_type, SUM(quantity) AS total_quantity FROM foodlistings GROUP BY food_type;'''),

    # ✅ Fixed Query 3: Contact info of food providers
    ("3. Contact info of providers by city (sample city: Mumbai)", 
     '''SELECT name, contact, city, type FROM providers WHERE city = 'Mumbai';'''),

    ("4. Receivers count by city", 
     '''SELECT city, COUNT(*) AS total_receivers FROM receivers GROUP BY city;'''),

    ("5. Food claims by status", 
     '''SELECT status, COUNT(*) AS total_claims FROM claims GROUP BY status;'''),

    ("6. Total meals listed by meal type", 
     '''SELECT meal_type, SUM(quantity) AS total_meals FROM foodlistings GROUP BY meal_type;'''),

    ("7. Most claimed food items", 
     '''SELECT f.food_name, COUNT(c.claim_id) AS total_claims 
        FROM foodlistings f 
        JOIN claims c ON f.food_id = c.food_id 
        GROUP BY f.food_name 
        ORDER BY total_claims DESC LIMIT 5;'''),

    ("8. Top 5 providers by total listings", 
     '''SELECT p.name, COUNT(f.food_id) AS total_listings 
        FROM providers p 
        JOIN foodlistings f ON p.provider_id = f.provider_id 
        GROUP BY p.name 
        ORDER BY total_listings DESC LIMIT 5;'''),

    ("9. Food quantity nearing expiry (next 3 days)", 
     '''SELECT food_name, quantity, expiry_date 
        FROM foodlistings 
        WHERE expiry_date <= CURRENT_DATE + INTERVAL '3 days';'''),

    ("10. Total quantity of food claimed (Approved only)", 
     '''SELECT SUM(f.quantity) AS total_claimed_quantity 
        FROM foodlistings f 
        JOIN claims c ON f.food_id = c.food_id 
        WHERE c.status = 'Approved';'''),

    ("11. Average quantity per listing", 
     '''SELECT AVG(quantity) AS avg_quantity FROM foodlistings;'''),

    # ✅ Verified Query 12
    ("12. City-wise approved claims", 
     '''SELECT r.city, COUNT(c.claim_id) AS approved_claims 
        FROM claims c 
        JOIN receivers r ON c.receiver_id = r.receiver_id 
        WHERE c.status = 'Approved' 
        GROUP BY r.city;'''),

    ("13. Pending claims by receiver", 
     '''SELECT r.name, COUNT(c.claim_id) AS pending_claims 
        FROM receivers r 
        JOIN claims c ON r.receiver_id = c.receiver_id 
        WHERE c.status = 'Pending' 
        GROUP BY r.name;'''),

    ("14. Top 5 cities with most food listings", 
     '''SELECT p.city, COUNT(*) AS total_listings 
        FROM providers p 
        JOIN foodlistings f ON p.provider_id = f.provider_id 
        GROUP BY p.city 
        ORDER BY total_listings DESC LIMIT 5;'''),

    ("15. Distribution of food types", 
     '''SELECT food_type, COUNT(*) AS count FROM foodlistings GROUP BY food_type;'''),

    ("16. Distribution of meal types", 
     '''SELECT meal_type, COUNT(*) AS count FROM foodlistings GROUP BY meal_type;'''),

    # ✅ Verified Query 17
    ("17. Provider types with most approved claims", 
     '''SELECT f.provider_type, COUNT(*) AS approved_claims 
        FROM foodlistings f 
        JOIN claims c ON f.food_id = c.food_id 
        WHERE c.status = 'Approved' 
        GROUP BY f.provider_type;'''),

    ("18. Expired food listings", 
     '''SELECT food_name, expiry_date FROM foodlistings WHERE expiry_date < CURRENT_DATE;'''),

    ("19. Total receivers by type", 
     '''SELECT type, COUNT(*) AS total FROM receivers GROUP BY type;'''),

    ("20. Provider listing activity", 
     '''SELECT p.name, COUNT(f.food_id) AS listings 
        FROM providers p 
        JOIN foodlistings f ON p.provider_id = f.provider_id 
        GROUP BY p.name;'''),

    ("21. Claim trends over time", 
     '''SELECT DATE(timestamp) AS claim_date, COUNT(*) AS num_claims 
        FROM claims 
        GROUP BY claim_date ORDER BY claim_date;'''),

    ("22. Recently added food listings", 
     '''SELECT food_name, quantity, expiry_date 
        FROM foodlistings 
        ORDER BY expiry_date DESC LIMIT 5;'''),

    ("23. Most active receivers", 
     '''SELECT r.name, COUNT(c.claim_id) AS total_claims 
        FROM receivers r 
        JOIN claims c ON r.receiver_id = c.receiver_id 
        GROUP BY r.name 
        ORDER BY total_claims DESC LIMIT 5;'''),

    ("24. Total claims per food type", 
     '''SELECT f.food_type, COUNT(c.claim_id) AS total_claims 
        FROM foodlistings f 
        JOIN claims c ON f.food_id = c.food_id 
        GROUP BY f.food_type;''')
]