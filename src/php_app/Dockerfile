FROM php:8.1-apache

# Install MySQL extension for PHP
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli

# Copy application code
COPY src/php_app/ /var/www/html/

# Set permissions
RUN chown -R www-data:www-data /var/www/html/
