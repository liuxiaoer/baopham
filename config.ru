require 'toto'
require File.expand_path('../hacks', __FILE__)
require 'rack/mobile-detect'

# Redirect to mobile site
use Rack::MobileDetect, :targeted => /BlackBerry|iPhone|Android/,
                        :redirect_to => 'http://m.example.com/'

# Rack config
use Rack::Static, 
    :urls => ['/css', '/js', '/images', '/favicon.ico', '/Resume.pdf', 'BingSiteAuth.xml', '/robots.txt'], 
    :root => 'public'
use Rack::CommonLogger

if ENV['RACK_ENV'] == 'development'
    use Rack::ShowExceptions
end

toto = Toto::Server.new do
    #
    # Add your settings here
    # set [:setting], [value]
    # 
    set :author,    "Bao Pham"                                  # blog author
    set :title,     "Bao Pham"
    set :url,       "http://bphamworld.heroku.com"
    set :root,      "index"                                     # page to load on /
    set :date,      lambda {|now| now.strftime("%d/%m/%Y") }    # date format for articles
    set :markdown,  :smart                                      # use markdown + smart-mode
    set :disqus,    true                                        # disqus id, or false
    set :summary,   :max => 150, :delim => /~/                  # length of article summary and delimiter
    set :ext,       'txt'                                       # file extension for articles
    set :cache,      7200                                       # cache duration, in seconds

    set :date,      lambda {|now| now.strftime("%B #{now.day.ordinal} %Y") }
    
    set :error,     lambda {|code|
        ERB.new(File.read("templates/pages/#{code}.rhtml")).result
    }
end

run toto

