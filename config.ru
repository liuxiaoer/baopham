require 'toto'
require File.expand_path('../sitemap', __FILE__)
require 'karakuri'

# Rack config
use Rack::Static,
    :urls => ['/css', '/js', '/img', '/favicon.ico', '/Resume.pdf', '/BingSiteAuth.xml', '/robots.txt', '/exclude.html'],
    :root => 'public'
use Rack::CommonLogger

if ENV['RACK_ENV'] == 'development'
    use Rack::ShowExceptions
end

Karakuri.link_format '<a href="/tagged?tag={tag}" title="articles with tag {tag}">{tag}</a> '

class Toto::Site
    alias_method :old_go, :go

    def go route, env = {}, type = :html
        if not route.first =~ /\d{4}/ and route.size == 2 and route.last =~ /(\d+)/
            @config[:id] = route.last.to_i
            route.pop
        end
        ret = old_go route, env, type
        @config.delete :id
        ret
    end
end

toto = Toto::Server.new do
    #
    # Add your settings here
    # set [:setting], [value]
    #
    set :author,    "Bao Pham"                                  # blog author
    set :title,     "Bao Pham"
    set :url,       "http://baopham.herokuapp.com"
    set :root,      "page"                                      # page to load on /
    set :articles_per_page,     6
    set :date,      lambda {|now| now.strftime("%d/%m/%Y") }    # date format for articles
    set :markdown,  :smart                                      # use markdown + smart-mode
    set :disqus,    "bpmsworld"                                 # disqus id, or false
    set :summary,   :max => 150, :delim => /~~~/                # length of article summary and delimiter
    set :ext,       'txt'                                       # file extension for articles
    set :cache,      28800                                      # cache duration, in seconds

    set :date,      lambda {|now| now.strftime("%B #{now.day.ordinal} %Y") }

    set :error,     lambda {|code|
        ERB.new(File.read("templates/pages/#{code}.rhtml")).result
    }
end

run toto

