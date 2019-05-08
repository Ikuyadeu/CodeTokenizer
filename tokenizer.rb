require "ripper"
require "json"

tokens = Ripper.lex(STDIN).map do |pos, type, str|
  {
    position: {
      line: pos[0],
      column: pos[1]
    },
    type: type.to_s.gsub(/^on_/, ""),
    string: str
  }
end

puts tokens.to_json

[].each do |x|
  foo(<<~EOF, "hello #{:world}", 'ho"\'ge')
    寿限無寿限無五劫のすり切れ
  EOF
end