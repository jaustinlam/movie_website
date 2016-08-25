import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
  "The story of a boy and his toys that come to life", 
  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print toy_story.storyline

avatar = media.Movie("Avatar", 
  "A marine on a alien planet", 
  "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
  "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print avatar.storyline
#avatar.show_trailer()

godfather = media.Movie("The Godfather",
  "Widely regarded as one of the greatest films of all time, this mob drama, based on Mario Puzo's novel of the same name, focuses on the powerful Italian-American crime family of Don Vito Corleone (Marlon Brando). When the don's youngest son, Michael (Al Pacino), reluctantly joins the Mafia, he becomes involved in the inevitable cycle of violence and betrayal. Although Michael tries to maintain a normal relationship with his wife, Kay (Diane Keaton), he is drawn deeper into the family business",
  "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
  "https://www.youtube.com/watch?v=sY1S34973zA")

#godfather.show_trailer()

bourne_identity = media.Movie("The Bourne Identity",
  "The story of a man (Matt Damon), salvaged, near death, from the ocean by an Italian fishing boat. When he recuperates, the man suffers from total amnesia, without identity or background... except for a range of extraordinary talents in fighting, linguistic skills and self-defense that speak of a dangerous past. He sets out on a desperate search-assisted by the initially rebellious Marie (Franka Potente) - to discover who he really is, and why he's being lethally pursued by assassins.",
  "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
  "https://www.youtube.com/watch?v=PGKK5wACwrU")

casino = media.Movie("Casino",
  "In early-1970s Las Vegas, low-level mobster Sam Acehttps://www.youtube.com/watch?v=8eCIRKJdV4k Rothstein (Robert De Niro) gets tapped by his bosses to head the Tangiers Casino. At first, he's a great success in the job, but over the years, problems with his loose-cannon enforcer Nicky Santoro (Joe Pesci), his ex-hustler wife Ginger (Sharon Stone), her con-artist ex Lester Diamond (James Woods) and a handful of corrupt politicians put Sam in ever-increasing danger. Martin Scorsese directs this adaptation of Nicholas Pileggi's book.",
  "https://upload.wikimedia.org/wikipedia/en/d/d8/Casino_poster.jpg",
  "https://www.youtube.com/watch?v=EGNx3ilNB80")

forrest_gump = media.Movie("Forrest Gump",
  "Slow-witted Forrest Gump (Tom Hanks) has never thought of himself as disadvantaged, and thanks to his supportive mother (Sally Field), he leads anything but a restricted life. Whether dominating on the gridiron as a college football star, fighting in Vietnam or captaining a shrimp boat, Forrest inspires people with his childlike optimism. But one person Forrest cares about most may be the most difficult to save -- his childhood love, the sweet but troubled Jenny (Robin Wright).",
  "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
  "https://www.youtube.com/watch?v=8eCIRKJdV4k")

movies = [avatar, godfather, bourne_identity, casino, forrest_gump]

fresh_tomatoes.open_movies_page(movies)





