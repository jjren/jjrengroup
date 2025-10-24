---
# Leave the homepage title empty to use the site title
title:
date: 2025-09-02
type: landing

sections:
  - block: slider
    content:
      slides:
      - title: 👋 Welcome to the Jiajun Ren Research Group @ Beijing Normal University 
        content: We develop accurate methods for efficient simulating quantum dynamics and dynamical properties of molecules and materials.
        align: center
        background:
          image:
            filename: welcome.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
      - title: Current Research Topics
        content: Electron-vibration coupled dynamics, tensor network, quantum algorithm 
        align: left
        background:
          image:
            filename: research.png
            filters:
              brightness: 0.7
          position: center
          color: '#555'
        link:
          icon: book-open
          icon_pack: fas
          text: Learn more
          url: ../research/

      - title: A Supportive and Collaborative Lab Environment
        content: 'We are seeking for researchers at all levels to join us!'
        align: center
        background:
          image:
            filename: group.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#333'
        link:
          icon: people-group
          icon_pack: fas
          text: Meet Us
          url: ../people/
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: '300px'
      is_fullscreen: true
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 3000
#  - block: hero
#    content:
#      title: |
#        Welcome to the Jiajun Ren Research Group @ BNU
#      image:
#        filename: welcome.jpg
#      text: |
#        <br>
#         
#         We develop accurate quantum chemistry methods for simulating structure and dynamics of molecules and materials.
   
#  - block: collection
#    content:
#      title: Latest News
#      subtitle:
#      text:
#      count: 5
#      filters:
#        author: ''
#        category: ''
#        exclude_featured: false
#        publication_type: ''
#        tag: ''
#      offset: 0
#      order: desc
#      page_type: post
#    design:
#      view: card
#      columns: '1'
#  
#  - block: markdown
#    content:
#      title:
#      subtitle: ''
#      text:
#    design:
#      columns: '1'
#      background:
#        image: 
#          filename: coders.jpg
#          filters:
#            brightness: 1
#          parallax: false
#          position: center
#          size: cover
#          text_color_light: true
#      spacing:
#        padding: ['20px', '0', '20px', '0']
#      css_class: fullscreen
#
#  - block: collection
#    content:
#      title: Latest Preprints
#      text: ""
#      count: 5
#      filters:
#        folders:
#          - publication
#        publication_type: 'article'
#    design:
#      view: citation
#      columns: '1'
#
#  - block: markdown
#    content:
#      title:
#      subtitle:
#      text: |
#        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
#    design:
#      columns: '1'
---
