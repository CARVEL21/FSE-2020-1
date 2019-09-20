/*Carvente Velasco Carlos Alberto
Hernandez Romero Pompeyo
FSE 2020-1 primer parcial
*/

/* UART asynchronous example, that uses separate RX and TX tasks

   This example code is in the Public Domain (or CC0 licensed, at your option.)

   Unless required by applicable law or agreed to in writing, this
   software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
   CONDITIONS OF ANY KIND, either express or implied.
*/

#include <stdlib.h>
#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_log.h"
#include "driver/uart.h"
#include "soc/uart_struct.h"
#include "string.h"
#include "driver/gpio.h"
#include "driver/adc.h"
#include "esp_adc_cal.h"

#define DEFAULT_VREF    3300        //Use adc2_vref_to_gpio() to obtain a better estimate
#define NO_OF_SAMPLES   64          //Multisampling

static const int RX_BUF_SIZE = 1024;

#define TXD_PIN 4
#define RXD_PIN 5

static esp_adc_cal_characteristics_t *adc_chars;
static const adc_channel_t channel = ADC_CHANNEL_6;     //GPIO34 if ADC1, GPIO14 if ADC2 no 0 porque esta ocupado
static const adc_atten_t atten = ADC_ATTEN_DB_11;// se configura la atenuacion de la entrada de voltaje
static const adc_unit_t unit = ADC_UNIT_1;


void init() {
    const uart_config_t uart_config = {
        .baud_rate = 115200,
        .data_bits = UART_DATA_8_BITS,
        .parity = UART_PARITY_DISABLE,
        .stop_bits = UART_STOP_BITS_1,
        .flow_ctrl = UART_HW_FLOWCTRL_DISABLE
    };
    uart_param_config(UART_NUM_1, &uart_config);
    //se utiliza el uart 1, porque la comunicacion no sera con la computadora
    uart_set_pin(UART_NUM_1, TXD_PIN, RXD_PIN, UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);
    // We won't use a buffer for sending data.
    uart_driver_install(UART_NUM_1, RX_BUF_SIZE * 2, 0, 0, NULL, 0);
}

int sendData(const char* logName, const char* data)
{
    //strcat(data, "\n");
    const int len = strlen(data);
    const int txBytes = uart_write_bytes(UART_NUM_1, data, len);
    printf("%s\n",data );
    //ESP_LOGI(logName, "Wrote %d bytes", txBytes);
    return txBytes;
}

static void tx_task()
{
    char enter;
    static const char *TX_TASK_TAG = "TX_TASK";
    //esp_log_level_set(TX_TASK_TAG, ESP_LOG_INFO);
    char data[RX_BUF_SIZE];
    double kelvin=0; 
    double celcius=0;
    while (scanf("%c",&enter)!= 1) {
        uint32_t adc_reading = 0;
        for (int i = 0; i < NO_OF_SAMPLES; i++){
            adc_reading += adc1_get_raw((adc1_channel_t)channel);
        }
        adc_reading /= NO_OF_SAMPLES;
        uint32_t voltage = esp_adc_cal_raw_to_voltage(adc_reading, adc_chars);
        kelvin=voltage/10; 
        celcius=kelvin-273.15f;
        //almacenamos la cadena con formato
        sprintf(data,"%d, %.2f, %.2f",voltage, kelvin, celcius);
        //sendData(TX_TASK_TAG, (const char *)data);
        sendData(TX_TASK_TAG, (const char *)data);
        vTaskDelay(2000 / portTICK_PERIOD_MS);
    }
    //free(data);
    //return 0; 
    //sendData(TX_TASK_TAG, NULL);
    vTaskDelete(NULL);
    //abort();
    //exit(0);
}
/*
//recibir esp, led
static void rx_task()
{
    static const char *RX_TASK_TAG = "RX_TASK";
    esp_log_level_set(RX_TASK_TAG, ESP_LOG_INFO);
    uint8_t* data = (uint8_t*) malloc(RX_BUF_SIZE+1);
    while (1) {
        const int rxBytes = uart_read_bytes(UART_NUM_1, data, RX_BUF_SIZE, 1000 / portTICK_RATE_MS);
        if (rxBytes > 0) {
            data[rxBytes] = 0;
            ESP_LOGI(RX_TASK_TAG, "Read %d bytes: '%s'", rxBytes, data);
            ESP_LOG_BUFFER_HEXDUMP(RX_TASK_TAG, data, rxBytes, ESP_LOG_INFO);
        }
    }
    free(data);
}*/

void app_main()
{
    init();
    if (unit == ADC_UNIT_1) {
        adc1_config_width(ADC_WIDTH_BIT_12);
        adc1_config_channel_atten(channel, atten);
    } else {
        adc2_config_channel_atten((adc2_channel_t)channel, atten);
    }
    //xTaskCreate(rx_task, "uart_rx_task", 1024*2, NULL, configMAX_PRIORITIES, NULL);
    adc_chars = calloc(1, sizeof(esp_adc_cal_characteristics_t));
    esp_adc_cal_value_t val_type = esp_adc_cal_characterize(unit, atten, ADC_WIDTH_BIT_12, DEFAULT_VREF, adc_chars);   
    xTaskCreate(tx_task, "uart_tx_task", 1024*2, NULL, configMAX_PRIORITIES-1, NULL);
}