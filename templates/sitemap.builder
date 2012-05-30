require 'karakuri'

xml.instruct!
xml.urlset("xmlns" => "http://www.sitemaps.org/schemas/sitemap/0.9") do

  xml.url do
    xml.loc @config[:url]
    xml.changefreq "weekly"
  end

  xml.url do
    xml.loc @config[:url] + '/resume'
    xml.changefreq "weekly"
  end

  xml.url do
    xml.loc @config[:url] + '/archives'
    xml.changefreq "weekly"
  end

  Karakuri::tag_cloud(articles).each do |tag, freq|
    xml.url do
      xml.loc @config[:url] + "/tagged?tag=#{tag}"
      xml.changefreq "weekly"
    end
  end

  articles.each do |article|
    xml.url do
      xml.loc @config[:url] + article.path
      xml.changefreq "weekly"
    end
  end

end
