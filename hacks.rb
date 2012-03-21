module Toto
    class Site
        def sitemap type = :xml
            {:articles => self.articles.map do |article|
                Article.new article, @config
            end}
        end
    end
end
