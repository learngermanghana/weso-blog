---
layout: page
title: Blogs
description: "Read practical blog articles on awareness, support, and educational improvement strategies."
pagination:
  enabled: true
  per_page: 10
  permalink: '/blogs/page:num/'
faq:
  - question: "What topics are covered in the blog?"
    answer: "The blog covers childhood cancer awareness, family support, and practical educational guidance."
  - question: "How do blog posts connect to tools and assessments?"
    answer: "Blog articles provide context and advice you can apply directly when using the course book and results pages."
---

<ul>
{% for post in site.posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <small>— {{ post.date | date: "%Y-%m-%d" }}</small>
  </li>
{% endfor %}
</ul>

{% include internal-links.html title="From reading to action" description="After reading, continue with the course book tools and assessment pages to apply what you learned." %}

{% if paginator.total_pages > 1 %}
<nav class="pagination" role="navigation">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path | relative_url }}" class="previous">&laquo; Previous</a>
  {% endif %}
  <span class="page-number">Page {{ paginator.page }} of {{ paginator.total_pages }}</span>
  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path | relative_url }}" class="next">Next &raquo;</a>
  {% endif %}
</nav>
{% endif %}
