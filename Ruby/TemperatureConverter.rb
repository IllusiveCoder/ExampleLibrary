
# Description: This program converts temperatures between Celsius and Fahrenheit.

class TemperatureConverter
    def celsius_to_fahrenheit(celsius)
      # Convert Celsius to Fahrenheit
      (celsius * 9.0 / 5.0) + 32
    end
  
    def fahrenheit_to_celsius(fahrenheit)
      # Convert Fahrenheit to Celsius
      (fahrenheit - 32) * 5.0 / 9.0
    end
  end
  
  # Usage example
  converter = TemperatureConverter.new
  celsius_temp = 25
  fahrenheit_temp = converter.celsius_to_fahrenheit(celsius_temp)
  puts "#{celsius_temp}°C is equal to #{fahrenheit_temp}°F"
  fahrenheit_temp = 77
  celsius_temp = converter.fahrenheit_to_celsius(fahrenheit_temp)
  puts "#{fahrenheit_temp}°F is equal to #{celsius_temp}°C"
  