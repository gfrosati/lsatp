require 'rubygems'
require 'bundler/setup'

require "wikipedia"

Wikipedia.Configure {
  domain 'es.wikipedia.org'
  path   'w/api.php'
}

for i in 1..1000
  page = Wikipedia.find_random()
  name = "articulos/" + page.fullurl.split("/").last
  File.open(name, 'w') { |file| file.write(page.text) }
end

