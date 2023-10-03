#!/usr/bin/env ruby
log_entry = ARGV[0]

from = log_entry.scan(/\[from:([^\]]+)\]/).join(",")
to = log_entry.scan(/\[to:([^\]]+)\]/).join(",")
flags = log_entry.scan(/\[flags:([^\]]+)\]/).join(",")

puts "#{from},#{to},#{flags}"
