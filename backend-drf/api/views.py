from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StockPredictionSerializer
from rest_framework import status
from rest_framework.response import Response
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
from django.conf import settings
from .utils import save_plot






# Create your views here.


class StockPredictionAPIView(APIView):
    def post(self, request):
        serializer = StockPredictionSerializer(data=request.data)
        if serializer.is_valid():
            ticker = serializer._validated_data['ticker']

            # Fetch data from yfinance
            now = datetime.now()
            start = datetime(now.year-10, now.month, now.day)
            end = now
            df = yf.download(ticker, start, end)
            if df.empty:
                return Response({"error": "No data found for the given ticker.",
                                "status": status.HTTP_404_NOT_FOUND})
            df = df.reset_index()

            # Generate Basic Plot
            plt.switch_backend('AGG')
            plt.figure(figsize=(12,5))
            plt.plot(df.Close, label='Closing Price')
            plt.title(f"Closing price of {ticker}")
            plt.xlabel('Days')
            plt.ylabel('Closed Price')
            plt.legend()
            # Save the plot to a file
            plot_img_path = f"{ticker}_plot.png"
            plot_img = save_plot(plot_img_path)

            # 100 days moving average
            ma100 = df.Close.rolling(100).mean()
            plt.switch_backend('AGG')
            plt.figure(figsize=(12,5))
            plt.plot(df.Close, label='Closing Price')
            plt.plot(ma100, 'r', label='100 DMA')
            plt.title(f"100 Days Moving Average of {ticker}")
            plt.xlabel('Days')
            plt.ylabel('Price')
            plt.legend()
            # Save the plot to a file
            plot_img_path = f"{ticker}_100_DMA.png"
            plot_100_dma = save_plot(plot_img_path)


            # 200 days moving average
            ma200 = df.Close.rolling(200).mean()
            plt.switch_backend('AGG')
            plt.figure(figsize=(12,5))
            plt.plot(df.Close, label='Closing Price')
            plt.plot(ma100, 'r', label='100 DMA')
            plt.plot(ma200, 'g', label='200 DMA')
            plt.title(f"200 Days Moving Average of {ticker}")
            plt.xlabel('Days')
            plt.ylabel('Price')
            plt.legend()
            # Save the plot to a file
            plot_img_path = f"{ticker}_200_DMA.png"
            plot_200_dma = save_plot(plot_img_path)


            return Response({'status': 'success',
                            'plot_img': plot_img,
                            'plot_100_dma': plot_100_dma,
                            'plot_200_dma': plot_200_dma})
