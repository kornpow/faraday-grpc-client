from .common import BaseClient, faradayrpc
from .errors import handle_rpc_errors


class FaradayClient(BaseClient):
    @handle_rpc_errors
    def channel_insights(self):
        """Unlock encrypted wallet at lnd startup"""
        request = faradayrpc.ChannelInsightsRequest()
        response = self._faraday_stub.ChannelInsights(request)
        return response

    @handle_rpc_errors
    def close_report(self, channel_point):
        """Unlock encrypted wallet at lnd startup"""
        request = faradayrpc.CloseReportRequest(channel_point=channel_point)
        response = self._faraday_stub.CloseReport(request)
        return response

    @handle_rpc_errors
    def exchange_rate(self):
        """Unlock encrypted wallet at lnd startup"""
        return "not implemented"
        request = faradayrpc.ExchangeRateRequest()
        response = self._faraday_stub.ExchangeRate(request)
        return response

    @handle_rpc_errors
    def node_audit(self):
        """Unlock encrypted wallet at lnd startup"""
        return "not implemented"
        request = faradayrpc.NodeAuditRequest()
        response = self._faraday_stub.NodeAudit(request)
        return response

    @handle_rpc_errors
    def outlier_recommendations(self):
        """Unlock encrypted wallet at lnd startup"""
        return "not implemented"
        request = faradayrpc.OutlierRecommendationsRequest()
        response = self._faraday_stub.OutlierRecommendations(request)
        return response

    @handle_rpc_errors
    def revenue_report(self):
        """Unlock encrypted wallet at lnd startup"""
        return "not implemented"
        request = faradayrpc.RevenueReportRequest()
        response = self._faraday_stub.RevenueReport(request)
        return response

    @handle_rpc_errors
    def threshold_recommendations(self):
        """Unlock encrypted wallet at lnd startup"""
        return "not implemented"
        request = faradayrpc.ThresholdRecommendationsRequest()
        response = self._faraday_stub.ThresholdRecommendations(request)
        return response