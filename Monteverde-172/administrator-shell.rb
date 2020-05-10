#!/usr/bin/ruby
require 'winrm'

conn = WinRM::Connection.new(
  endpoint: 'http://10.10.10.172:5985/wsman',
  user: 'Administrator',
  password: 'd0m@in4dminyeah!',
)

command=""

conn.shell(:powershell) do |shell|
    until command == "exit\n" do
        print "PS > "
        command = gets
        output = shell.run(command) do |stdout, stderr|
            STDOUT.print stdout
            STDERR.print stderr
        end
    end
    puts "Exiting with code #{output.exitcode}"
end
