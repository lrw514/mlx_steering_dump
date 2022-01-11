#SPDX-License-Identifier: BSD-3-Clause
#Copyright (c) 2021 NVIDIA CORPORATION. All rights reserved.

from hw_steering_src.dr_common import *


class dr_parse_context():
    def __init__(self, data):
        keys = ["mlx5dr_debug_res_type", "id", "hws_support",
                "dev_name", "package_version"]
        self.data = dict(zip(keys, data + [None] * (len(keys) - len(data))))
        self.fix_data()
        self.tables = []
        self.attr = None
        self.caps = None
        self.send_engine = []

    def dump_str(self, verbosity):
        return dump_obj_str(["mlx5dr_debug_res_type", "id",
                             "hws_support", "dev_name", "package_version"],
                             self.data)

    def tree_print(self, verbosity, tabs):
        _str = tabs + self.dump_str(verbosity)
        tabs = tabs + TAB

        _str = _str + tabs + self.attr.dump_str(verbosity)

        if verbosity > 0:
            _str = _str + tabs + self.caps.dump_str(verbosity)

        if verbosity > 2:
            for se in self.send_engine:
                _str = _str + se.tree_print(verbosity, tabs)

        for t in self.tables:
            _str = _str + t.tree_print(verbosity, tabs)

        return _str

    def fix_data(self):
        self.data["hws_support"] = "True" if self.data["hws_support"] is "1" else "False"

    def add_table(self, table):
        self.tables.append(table)

    def add_attr(self, attr):
        self.attr = attr

    def add_caps(self, caps):
        self.caps = caps

    def add_send_engine(self, send_engine):
        self.send_engine.append(send_engine)


class dr_parse_context_attr():
    def __init__(self, data):
        keys = ["mlx5dr_debug_res_type", "ctx_id",
                "pd_num", "queues", "queue_size"]
        self.data = dict(zip(keys, data + [None] * (len(keys) - len(data))))

    def dump_str(self, verbosity):
        return dump_obj_str(["mlx5dr_debug_res_type", "ctx_id",
                             "pd_num", "queues", "queue_size"],
                             self.data)


class dr_parse_context_caps():
    def __init__(self, data):
        keys = ["mlx5dr_debug_res_type", "ctx_id", "fw_version",
                "wqe_based_update", "ste_format", "ste_alloc_log_max",
                "log_header_modify_argument_max_alloc", "flex_protocols",
                "rtc_reparse_mode", "rtc_index_mode", "ste_alloc_log_gran",
                "stc_alloc_log_max", "stc_alloc_log_gran", "fdb_ft_reparse",
                "rtc_log_depth_max", "flex_parser_id_gtpu_dw_0",
                "flex_parser_id_gtpu_teid", "flex_parser_id_gtpu_dw_2",
                "flex_parser_id_gtpu_first_ext_dw_0", "nic_ft_max_level",
                "nic_ft_reparse", "fdb_ft_max_level", "fdb_ft_reparse",
                "log_header_modify_argument_granularity"]
        self.data = dict(zip(keys, data + [None] * (len(keys) - len(data))))

    def dump_str(self, verbosity):
        _keys = ["mlx5dr_debug_res_type", "ctx_id"]
        if verbosity > 0:
            _keys.extend(["fw_version", "wqe_based_update",
                          "ste_format", "ste_alloc_log_max",
                          "log_header_modify_argument_max_alloc"])
        if verbosity == 2:
            _keys.extend(["flex_protocols", "rtc_reparse_mode",
                          "rtc_index_mode", "ste_alloc_log_gran",
                          "stc_alloc_log_max", "stc_alloc_log_gran",
                          "fdb_ft_reparse", "rtc_log_depth_max",
                          "flex_parser_id_gtpu_dw_0",
                          "flex_parser_id_gtpu_teid",
                          "flex_parser_id_gtpu_dw_2",
                          "flex_parser_id_gtpu_first_ext_dw_0",
                          "nic_ft_max_level", "nic_ft_reparse",
                          "fdb_ft_max_level", "fdb_ft_reparse",
                          "log_header_modify_argument_granularity"])

        return dump_obj_str(_keys, self.data)


class dr_parse_context_send_engine():
    def __init__(self, data):
        keys = ["mlx5dr_debug_res_type", "ctx_id", "id", "used_entries",
                "th_entries", "rings", "num_entries", "err", "ci", "pi",
                "completed_mask"]
        self.data = dict(zip(keys, data + [None] * (len(keys) - len(data))))
        self.send_ring = []

    def dump_str(self, verbosity):
        return dump_obj_str(["mlx5dr_debug_res_type", "ctx_id", "id",
                             "used_entries", "th_entries", "rings",
                             "num_entries", "err", "ci", "pi"], self.data)

    def tree_print(self, verbosity, tabs):
        _str = tabs + self.dump_str(verbosity)
        tabs = tabs + TAB

        for sr in self.send_ring:
            _str = _str + tabs + sr.dump_str(verbosity)

        return _str

    def add_send_ring(self, send_ring):
        self.send_ring.append(send_ring)


class dr_parse_context_send_ring():
    def __init__(self, data):
        keys = ["mlx5dr_debug_res_type", "ctx_id", "id", "send_engine_index",
                "cqn", "cq_cons_index", "cq_ncqe_mask", "cq_buf_sz",
                "cq_ncqe", "cq_cqe_log_sz", "cq_poll_wqe", "cq_cqe_sz", "sqn",
                "sq_obj_id", "sq_cur_post", "sq_buf_mask"]
        self.data = dict(zip(keys, data + [None] * (len(keys) - len(data))))

    def dump_str(self, verbosity):
        return dump_obj_str(["mlx5dr_debug_res_type", "ctx_id", "id",
                             "send_engine_index", "cqn", "cq_cons_index",
                             "cq_ncqe_mask", "cq_buf_sz", "cq_ncqe",
                             "cq_cqe_log_sz", "cq_poll_wqe", "cq_cqe_sz",
                             "sqn", "sq_obj_id", "sq_cur_post",
                             "sq_buf_mask"], self.data)