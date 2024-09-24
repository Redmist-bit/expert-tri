{
    'name': 'custom_web',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Custom content bar animation',
    'description': 'Adds a continuous animated content bar to the website.',
    'author': 'Your Name',
   'depends': ['base', 'website', 'web_editor', 'animated_snippet', 'hr_contract'],
    'data': [
        'views/snippets/snippets.xml',
        'views/snippets/a_content_bar_templates.xml',
        'views/snippets/a_content_service_templates.xml',
        'views/snippets/a_content_slideshow_testimonial_template.xml',
        'views/contract.xml'
    ],
     'assets': {
        'web.assets_frontend': [
            '/custom_web/static/src/css/a_content_bar.css',
            '/custom_web/static/src/css/a_content_service.css',
            '/custom_web/static/src/css/a_content_slideshow_testimonial.css',
            
        ],
        # 'web.assets_qweb': ['/custom_web/static/src/js/custom_script.js',]
     },


    'installable': True,
    'application': False,
}
