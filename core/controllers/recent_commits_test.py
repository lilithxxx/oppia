# coding: utf-8
#
# Copyright 2018 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for recent commit controllers."""

from core.platform import models
from core.tests import test_utils
import feconf

(exp_models,) = models.Registry.import_models([models.NAMES.exploration])


class RecentCommitsHandlerUnitTests(test_utils.GenericTestBase):
    """Test the RecentCommitsHandler class."""

    def setUp(self):
        super(RecentCommitsHandlerUnitTests, self).setUp()
        self.signup(self.MODERATOR_EMAIL, self.MODERATOR_USERNAME)
        self.set_moderators([self.MODERATOR_USERNAME])

        commit1 = exp_models.ExplorationCommitLogEntryModel.create(
            'entity_1', 0, 'committer_0', 'Janet',
            'create', 'created first commit', [], 'public', True)
        commit2 = exp_models.ExplorationCommitLogEntryModel.create(
            'entity_1', 1, 'committer_1', 'Joe',
            'edit', 'edited commit', [], 'public', True)
        commit3 = exp_models.ExplorationCommitLogEntryModel.create(
            'entity_2', 0, 'committer_0', 'Janet',
            'create', 'created second commit', [], 'private', False)
        commit1.exploration_id = 'exp_1'
        commit2.exploration_id = 'exp_1'
        commit3.exploration_id = 'exp_2'
        commit1.put()
        commit2.put()
        commit3.put()
