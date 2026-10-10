import works.models
from django.db import migrations, models


STORIES = [
    (
        "Arjun & Ankita",
        "Arjun and Ankita first crossed paths during their college cultural festival. Among the chaos of music, laughter, and lights, their eyes met across the crowd. Arjun, with a shy smile, offered her a cup of coffee, and that simple gesture turned into hours of conversation. What began as a casual friendship slowly turned into love at first sight. Their bond grew stronger with every passing day, and soon they found themselves planning small adventures together. Their most cherished memory was their trip to Darjeeling, where they walked hand in hand through the misty hills, capturing countless photographs against the backdrop of the tea gardens and snowy Kanchenjunga. To this day, they believe that their love story began with one accidental glance that changed everything forever.",
        "works/images/aa1.jpeg",
    ),
    (
        "Rohan & Priya",
        "Rohan and Priya met for the first time at their office cafeteria. Priya was searching for a seat during a busy lunch hour, and Rohan offered her a chair at his table. That small act of kindness sparked a beautiful connection. Their first official outing was at the famous Kolkata Book Fair, where they spent an entire evening exploring books, sharing childhood memories, and laughing over coffee. From there, their story unfolded like a fairy tale. They visited Puri together to watch the sunrise at the beach, walked barefoot on the sand, and clicked endless pictures while the waves crashed gently in the background. Each memory became a building block of their love, and their journey is proof that love at first sight can truly blossom into a lifetime of happiness.",
        "works/images/aa3.jpeg",
    ),
    (
        "Sourav & Neha",
        "Sourav and Neha’s story began at a friend’s wedding. Amidst the bright lights, music, and laughter, they were introduced casually by a mutual friend. But the moment Sourav looked into Neha’s eyes, he knew something had changed forever. They started with long conversations and a movie outing that turned into their very first date. Slowly but surely, their connection deepened. Their most memorable trip was to Jaipur, the Pink City, where they explored palaces, rode camels through the desert, and shared countless laughs under the starlit sky. For them, love at first sight was not just a phrase — it was the magical beginning of a journey filled with trust, laughter, and unforgettable adventures.",
        "works/images/aa2.jpeg",
    ),
    (
        "Aditya & Sneha",
        "Aditya and Sneha first met during their school reunion after many years apart. What started as a casual conversation about old memories soon turned into endless laughter and comfort. Their first date was at the iconic Coffee House in Kolkata, where they spoke for hours as if they had known each other all their lives. Soon, they planned a trip to Shimla together, where their love story blossomed amidst the snowy mountains and cozy evenings. They played in the snow, clicked silly pictures, and created unforgettable memories. For Aditya and Sneha, their reunion was more than nostalgia — it was destiny giving them a second chance at love, proving that first looks can sometimes bring back lost souls together.",
        "works/images/aa4.jpeg",
    ),
    (
        "Rahul & Meera",
        "Rahul and Meera’s story began in the quiet corners of a library. Rahul noticed Meera deeply lost in a book, and he couldn’t resist striking up a conversation. That first conversation lasted hours, and they quickly realized how much they had in common. Their bond grew through endless discussions about books, dreams, and life. Their love story blossomed with little coffee dates, late-night calls, and finally, a romantic trip to the backwaters of Kerala. Floating in a houseboat surrounded by serene waters, they captured the essence of peace and love in countless photographs. Rahul and Meera’s story is a reminder that sometimes love stories begin in the most unexpected, silent places — with a first glance that changes everything.",
        "works/images/aa5.jpeg",
    ),
    (
        "Kunal & Ishita",
        "Kunal and Ishita met for the first time at a friend’s birthday celebration. Surrounded by balloons, laughter, and music, they were introduced to each other and instantly felt a spark. Their very first outing together was nothing fancy — just an evening walk followed by ice-cream from a local shop. But in that simple moment, they realized how much they enjoyed each other’s company. Their bond grew stronger over countless conversations, long drives, and late-night chats. Soon, they planned a trip to Goa, where they walked along the beaches, watched sunsets together, and captured beautiful moments in photographs. For Kunal and Ishita, love at first sight was just the beginning of a journey full of laughter, companionship, and everlasting memories.",
        "works/images/aa6.jpeg",
    ),
    (
        "Dev & Ananya",
        "Dev first saw Ananya in a college library, where she was deeply engrossed in a book. Her calm aura, the way she twirled her hair while reading, and the little smile that appeared on her lips instantly caught his attention. Dev, who usually avoided unnecessary conversations, gathered the courage to ask about the book. That simple question became the beginning of endless talks. They soon discovered their mutual love for literature, coffee shops, and midnight walks. Their first trip was to Shimla, where they spent hours walking in the chilly breeze, sipping hot chocolate, and laughing under starry skies. For them, love at first sight was the spark, but the warmth of countless shared dreams turned it into a forever bond.",
        "works/images/aa7.jpeg",
    ),
    (
        "Arnav & Riya",
        "Arnav and Riya’s love story began at a wedding, where Riya was dancing with her cousins. Arnav noticed her vibrant energy, the sparkle in her eyes, and the way she enjoyed every moment as if the world belonged to her. Their first conversation started with a silly argument about music preferences but ended with both of them laughing uncontrollably. Soon after, they began meeting secretly at a lakeside park, where they talked about life, dreams, and everything in between. Their journey took them to Udaipur, where they explored palaces, boat rides, and candlelight dinners under moonlit skies. The magic of that first glance stayed alive in every heartbeat they shared.",
        "works/images/aa8.jpeg",
    ),
    (
        "Kabir & Aisha",
        "Kabir met Aisha on a rainy evening at a bus stop. Aisha stood there holding an umbrella, and when Kabir came drenched, she quietly extended it towards him without saying a word. That single gesture created a connection stronger than words. They began meeting often, sometimes just sharing coffee in silence, other times discussing dreams of traveling the world. Their first trip was to Kerala, where they sailed through backwaters, clicked countless photos amidst palm trees, and promised to hold onto each other forever. Love at first sight for them was not just about attraction — it was the beginning of kindness, respect, and a soulful companionship.",
        "works/images/aa9.jpeg",
    ),
    (
        "Veer & Myra",
        "Veer first met Myra at an art exhibition. While Myra admired a painting, Veer, an artist himself, noticed her eyes glowing with curiosity. They exchanged a few words about colors, but that conversation led to hours of laughter and a sudden bond. Their first outing was in Delhi, where they explored historical monuments, took selfies at every corner, and ended the evening with street food adventures. Later, they traveled to Manali, where they danced in snowfall, clicked romantic pictures, and realized how complete they felt with each other. Their first look turned into a masterpiece of love and togetherness.",
        "works/images/aa10.jpeg",
    ),
    (
        "Rehan & Zoya",
        "Rehan and Zoya met in a bookstore, both reaching for the same novel at the exact moment. Their hands touched, their eyes met, and time seemed to freeze. That accidental meeting turned into an everyday ritual, where they started visiting cafes, talking endlessly, and enjoying late-night drives under the stars. Their first big trip was to Jaipur, where they explored forts, enjoyed camel rides, and captured candid pictures against royal backdrops. What began as a magical glance soon grew into an eternal love story, filled with adventure, laughter, and soulful memories.",
        "works/images/aa11.jpeg",
    ),
    (
        "Ishan & Tara",
        "Ishan saw Tara for the first time at a charity event, where she was helping children with a bright smile on her face. That moment, her kindness touched his heart deeply. They started talking over coffee, and soon realized they shared similar dreams of traveling and creating memories together. Their very first trip was to Darjeeling, where they took toy train rides, watched the sunrise from Tiger Hill, and clicked countless photographs together. From that first look of admiration grew a love story that was pure, passionate, and inspiring for everyone around them.",
        "works/images/aa12.jpeg",
    ),
]


def add_existing_stories(apps, schema_editor):
    Firstlook = apps.get_model("works", "Firstlook")
    database = schema_editor.connection.alias
    for title, description, image_path in STORIES:
        Firstlook.objects.using(database).get_or_create(
            title=title,
            defaults={"description": description, "image_path": image_path},
        )


class Migration(migrations.Migration):
    dependencies = [
        ("works", "0004_alter_firstlook_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="firstlook",
            name="image_path",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="firstlook",
            name="image",
            field=models.ImageField(
                blank=True,
                upload_to=works.models.firstlook_image_upload_to,
            ),
        ),
        migrations.RunPython(add_existing_stories, migrations.RunPython.noop),
    ]
