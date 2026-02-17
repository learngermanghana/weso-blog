from __future__ import annotations

import argparse
from datetime import date, datetime
from pathlib import Path
import re

POSTS_DIR = Path("_posts")


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return (text[:90].strip("-") or "post")


def build_post(
    title: str,
    excerpt: str,
    category: str,
    tags: list[str],
    image_url: str,
    image_alt: str,
    permalink_slug: str,
    seo_title: str,
    seo_description: str,
    body: str,
    publish_date: str,
) -> str:
    tag_string = ", ".join(tags)

    fm = [
        "---",
        "layout: post",
        f'title: "{title}"',
        f"date: {publish_date}",
        f"tags: [{tag_string}]",
        f"categories: [{category}]",
        f'excerpt: "{excerpt}"',
        f"image: {image_url}",
        f'image_alt: "{image_alt}"',
        f"permalink: /{permalink_slug}/",
        "seo:",
        f'  title: "{seo_title}"',
        f'  description: "{seo_description}"',
        "---",
        "",
    ]
    return "\n".join(fm) + body.strip() + "\n"


def build_structured_body(
    intro_heading: str,
    intro_lines: list[str],
    sections: list[dict],
    quick_points: list[str],
    action_items: list[str],
    final_lines: list[str],
) -> str:
    lines = [f"## {intro_heading}"]
    lines.extend(intro_lines)
    lines.append("")
    lines.append("---")
    lines.append("")

    for idx, section in enumerate(sections, 1):
        lines.append(f"## {idx}. **{section['title']}**")
        lines.extend(section["explanation"])
        lines.append("")
        lines.append("**Examples**")
        for example in section["examples"]:
            lines.append(f"- {example}")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## Quick points")
    for point in quick_points:
        lines.append(f"- {point}")

    lines += ["", "---", "", "## How you can help today"]
    for item in action_items:
        lines.append(f"- {item}")

    lines += ["", "---", "", "## Final note"]
    lines.extend(final_lines)
    lines += ["", "👉 Donate • Volunteer • Partner with **Wesoamo Child Cancer Foundation**"]
    return "\n".join(lines)


def awareness_body() -> str:
    return build_structured_body(
        intro_heading="Why childhood cancer awareness matters",
        intro_lines=[
            "Early recognition can reduce delays in treatment and improve outcomes.",
            "Communities, schools, and faith groups all play a role in sharing life-saving information.",
        ],
        sections=[
            {
                "title": "Know common warning signs",
                "explanation": ["Persistent symptoms should be checked by a health professional as early as possible."],
                "examples": [
                    "Unexplained weight loss or prolonged fever",
                    "Frequent unexplained bruising or bleeding",
                    "Persistent headaches, vomiting, or unusual swelling",
                ],
            },
            {
                "title": "Act quickly and seek care",
                "explanation": ["Timely referral to a hospital can make a major difference for the child and family."],
                "examples": [
                    "Encourage parents to visit qualified health facilities",
                    "Help families access referral information and transport options",
                ],
            },
        ],
        quick_points=[
            "Awareness can reduce late diagnosis.",
            "Simple community education saves time and stress for families.",
            "Trusted local voices help break myths and fear.",
        ],
        action_items=[
            "Share one verified awareness message this week.",
            "Invite a health professional for a short community talk.",
            "Support outreach campaigns in schools and churches/mosques.",
        ],
        final_lines=[
            "When we spread accurate information, families can seek help earlier.",
            "Awareness is one of the most powerful forms of support we can offer.",
        ],
    )


def support_body() -> str:
    return build_structured_body(
        intro_heading="Supporting treatment journeys with dignity",
        intro_lines=[
            "Families facing childhood cancer often carry medical, emotional, and financial burdens at once.",
            "Practical support can ease pressure and help children stay on treatment.",
        ],
        sections=[
            {
                "title": "Welfare and emergency support",
                "explanation": ["Small interventions can prevent interruptions in treatment and reduce distress."],
                "examples": [
                    "Transport support for hospital visits",
                    "Essential supplies for children in treatment",
                    "Emergency relief for urgent family needs",
                ],
            },
            {
                "title": "Parent counselling and emotional care",
                "explanation": ["Parents need safe spaces to process difficult diagnoses and care decisions."],
                "examples": [
                    "Counselling check-ins during treatment",
                    "Guidance and referrals where needed",
                ],
            },
        ],
        quick_points=[
            "Compassion and privacy are central to our work.",
            "Family wellbeing influences treatment consistency.",
            "Long-term follow-up supports recovery and reintegration.",
        ],
        action_items=[
            "Donate toward welfare and treatment support.",
            "Volunteer skills for outreach, counselling support, or logistics.",
            "Partner with us on hospital child welfare projects.",
        ],
        final_lines=[
            "No parent should walk this journey alone.",
            "Together, we can provide hope, dignity, and practical support.",
        ],
    )


def week_index_utc() -> int:
    return date.today().isocalendar().week


def get_topic_for_week(week_index: int) -> dict:
    topics = [
        {
            "title": "Early Signs of Childhood Cancer Every Parent Should Know",
            "excerpt": "A practical guide to warning signs and why early hospital care matters.",
            "category": "Awareness",
            "tags": ["childhood cancer", "awareness", "ghana", "parents"],
            "image": "https://images.pexels.com/photos/6753163/pexels-photo-6753163.jpeg",
            "image_alt": "Doctor speaking with parent and child in a clinic",
            "seo_title": "Early Signs of Childhood Cancer: Parent Awareness Guide",
            "seo_description": "Learn key warning signs of childhood cancer and how early action can support better outcomes for children.",
            "permalink_slug": "early-signs-of-childhood-cancer-parents-guide",
            "body": awareness_body(),
        },
        {
            "title": "Hope, Dignity, and Support for Children Fighting Cancer",
            "excerpt": "How compassionate welfare support helps children and families through treatment.",
            "category": "Support",
            "tags": ["childhood cancer", "support", "welfare", "ghana"],
            "image": "https://images.pexels.com/photos/7551674/pexels-photo-7551674.jpeg",
            "image_alt": "Caregiver comforting a child",
            "seo_title": "Hope and Dignity for Children Fighting Cancer in Ghana",
            "seo_description": "See how welfare and emotional support can reduce burden for children in treatment and their families.",
            "permalink_slug": "hope-dignity-support-for-children-fighting-cancer",
            "body": support_body(),
        },
        {
            "title": "Why Childhood Cancer Awareness Campaigns Save Lives",
            "excerpt": "Community awareness helps families recognize symptoms early and seek care quickly.",
            "category": "Awareness",
            "tags": ["awareness", "community", "childhood cancer", "ghana"],
            "image": "https://images.pexels.com/photos/6646917/pexels-photo-6646917.jpeg",
            "image_alt": "Community health education session",
            "seo_title": "Childhood Cancer Awareness Campaigns in Ghana",
            "seo_description": "Understand why community campaigns are critical for early detection and timely hospital referral.",
            "permalink_slug": "childhood-cancer-awareness-campaigns-save-lives",
            "body": awareness_body(),
        },
        {
            "title": "Financial and Welfare Support: What Families Need Most",
            "excerpt": "A look at practical needs families face during childhood cancer treatment.",
            "category": "Support",
            "tags": ["financial support", "welfare", "families", "childhood cancer"],
            "image": "https://images.pexels.com/photos/4386466/pexels-photo-4386466.jpeg",
            "image_alt": "Parent and child holding hands in hospital",
            "seo_title": "Financial and Welfare Support for Childhood Cancer Families",
            "seo_description": "Explore priority welfare and financial needs for families caring for children undergoing cancer treatment.",
            "permalink_slug": "financial-welfare-support-for-families",
            "body": support_body(),
        },
        {
            "title": "Standing with Parents Through Difficult Diagnoses",
            "excerpt": "Why counselling and emotional support matter for parents and caregivers.",
            "category": "Counselling",
            "tags": ["counselling", "parents", "emotional support", "ghana"],
            "image": "https://images.pexels.com/photos/7176305/pexels-photo-7176305.jpeg",
            "image_alt": "Counsellor supporting a parent",
            "seo_title": "Parent Counselling and Emotional Support in Childhood Cancer",
            "seo_description": "Learn how counselling support helps parents cope, make decisions, and sustain care for their children.",
            "permalink_slug": "standing-with-parents-through-difficult-diagnoses",
            "body": support_body(),
        },
        {
            "title": "Survivor Follow-Up: Life After Childhood Cancer Treatment",
            "excerpt": "Follow-up support helps survivors heal, grow in confidence, and reintegrate.",
            "category": "Survivorship",
            "tags": ["survivor follow-up", "childhood cancer", "reintegration", "ghana"],
            "image": "https://images.pexels.com/photos/3768166/pexels-photo-3768166.jpeg",
            "image_alt": "Young survivor smiling outdoors",
            "seo_title": "Survivor Follow-Up Support After Childhood Cancer",
            "seo_description": "Discover why survivor follow-up is essential for emotional wellbeing, confidence, and reintegration.",
            "permalink_slug": "survivor-follow-up-after-childhood-cancer-treatment",
            "body": support_body(),
        },
        {
            "title": "Hospital Child Welfare Projects That Bring Comfort",
            "excerpt": "How child-focused hospital projects improve dignity and comfort during treatment.",
            "category": "Projects",
            "tags": ["hospital projects", "child welfare", "support", "ghana"],
            "image": "https://images.pexels.com/photos/1257110/pexels-photo-1257110.jpeg",
            "image_alt": "Colorful child-friendly hospital room",
            "seo_title": "Hospital Child Welfare Projects for Children in Treatment",
            "seo_description": "See how child welfare projects in hospitals can provide comfort and dignity to young patients.",
            "permalink_slug": "hospital-child-welfare-projects-bring-comfort",
            "body": support_body(),
        },
        {
            "title": "How Volunteers Can Make a Difference for Families",
            "excerpt": "Simple volunteer actions can reduce stress and strengthen family support systems.",
            "category": "Get Involved",
            "tags": ["volunteer", "community", "family support", "childhood cancer"],
            "image": "https://images.pexels.com/photos/6646918/pexels-photo-6646918.jpeg",
            "image_alt": "Volunteers engaging with families",
            "seo_title": "Volunteer Support for Childhood Cancer Families",
            "seo_description": "Learn practical ways volunteers can support children in treatment and their families in Ghana.",
            "permalink_slug": "how-volunteers-can-make-a-difference",
            "body": support_body(),
        },
        {
            "title": "Community Partnerships for Better Childhood Cancer Care",
            "excerpt": "Partnerships with communities and institutions expand support for children and parents.",
            "category": "Partnerships",
            "tags": ["partnership", "community", "awareness", "support"],
            "image": "https://images.pexels.com/photos/3184338/pexels-photo-3184338.jpeg",
            "image_alt": "Group partnership meeting",
            "seo_title": "Community Partnerships for Childhood Cancer Support",
            "seo_description": "Strong partnerships help scale awareness, welfare support, and counselling for families.",
            "permalink_slug": "community-partnerships-for-better-childhood-cancer-care",
            "body": awareness_body(),
        },
        {
            "title": "Transparent Giving: How Donations Support Real Needs",
            "excerpt": "Transparency builds trust and ensures support reaches children and families effectively.",
            "category": "Donate",
            "tags": ["donate", "transparency", "welfare", "charity"],
            "image": "https://images.pexels.com/photos/6647037/pexels-photo-6647037.jpeg",
            "image_alt": "Hands giving donation envelope",
            "seo_title": "Transparent Giving for Childhood Cancer Support",
            "seo_description": "Understand how transparent charitable giving can support practical needs for children in treatment.",
            "permalink_slug": "transparent-giving-how-donations-support-real-needs",
            "body": support_body(),
        },
    ]

    idx = (week_index - 1) % len(topics)
    return topics[idx]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate one weekly blog post in _posts/.")
    parser.add_argument("--date", help="Publishing date in YYYY-MM-DD format (default: current UTC date).")
    parser.add_argument(
        "--week-index",
        type=int,
        help="ISO week index override for topic rotation (default: current ISO week).",
    )
    parser.add_argument("--force", action="store_true", help="Create a file even if one with the same name already exists.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned filename/topic and exit without writing files.")
    return parser.parse_args()


def resolve_publish_date(raw_date: str | None) -> str:
    if raw_date is None:
        return datetime.utcnow().strftime("%Y-%m-%d")

    datetime.strptime(raw_date, "%Y-%m-%d")
    return raw_date


def post_already_contains_title(title: str) -> bool:
    escaped_title = re.escape(f'title: "{title}"')
    title_pattern = re.compile(rf"^{escaped_title}$", re.MULTILINE)
    for post_file in POSTS_DIR.glob("*.md"):
        if title_pattern.search(post_file.read_text(encoding="utf-8")):
            return True
    return False


def main() -> int:
    args = parse_args()
    POSTS_DIR.mkdir(parents=True, exist_ok=True)

    selected_week_index = args.week_index or week_index_utc()
    topic = get_topic_for_week(selected_week_index)

    publish_date = resolve_publish_date(args.date)
    slug = slugify(topic["title"])
    filename = f"{publish_date}-{slug}.md"
    path = POSTS_DIR / filename

    if args.dry_run:
        print(f"[dry-run] Week index: {selected_week_index}")
        print(f"[dry-run] Topic: {topic['title']}")
        print(f"[dry-run] Target file: {path}")
        return 0

    if path.exists() and not args.force:
        print(f"Post already exists: {path}")
        return 0

    if post_already_contains_title(topic["title"]) and not args.force:
        print(f"Post with this title already exists: {topic['title']}")
        return 0

    md = build_post(
        title=topic["title"],
        excerpt=topic["excerpt"],
        category=topic["category"],
        tags=topic["tags"],
        image_url=topic["image"],
        image_alt=topic["image_alt"],
        permalink_slug=topic["permalink_slug"],
        seo_title=topic["seo_title"],
        seo_description=topic["seo_description"],
        body=topic["body"],
        publish_date=publish_date,
    )

    path.write_text(md, encoding="utf-8")
    print(f"Created: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
